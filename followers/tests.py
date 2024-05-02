from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower
from django.contrib.auth.models import User


class FollowerListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')

    def test_can_list_followers(self):
        bob = User.objects.get(username='bob')
        followed = User.objects.get(username='bill')
        Follower.objects.create(owner=bob, followed=followed)
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_follow_user(self):
        self.client.login(username='bob', password='pass')
        followed = User.objects.get(username='bill')
        response = self.client.post('/followers/', {'followed': 2, 'followed_name':'bill'})
        count = Follower.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_follow_user(self):
        response = self.client.post('/followers/', {'followed': 2, 'followed_name':'bill'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        followed = User.objects.create_user(username='bill', password='pass')
        Follower.objects.create(
            owner=bob, followed=followed
        )    

    def test_can_retrieve_follower_using_valid_id(self):
        response = self.client.get('/followers/1/')
        self.assertEqual(response.data['owner'], 'bob')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_follower_using_invalid_id(self):
        response = self.client.get('/followers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow_user(self):
        self.client.login(username='bob', password='pass')
        url = reversed('/followers/1/')
        data = {'followed': 2}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
