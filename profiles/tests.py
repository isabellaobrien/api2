from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile
from django.contrib.auth.models import User


class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')

    def test_can_list_profiles(self):
        bob = User.objects.get(username='bob')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfilesDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'bob')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        self.client.login(username='bob', password='pass')
        response = self.client.put('/profiles/1/', {'name': 'bob', 'about_me':'new about me'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.about_me, 'new about me')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_profile(self):
        self.client.login(username='bob', password='pass')
        response = self.client.put('/profiles/2/', {'name': 'bill', 'about_me':'new about me'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
