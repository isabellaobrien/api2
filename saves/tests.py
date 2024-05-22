from rest_framework import status
from rest_framework.test import APITestCase
from stories.models import Story
from .models import Save
from django.contrib.auth.models import User


class SaveListViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')

    def test_can_list_saves(self):
        bob = User.objects.get(username='bob')
        bill = User.objects.get(username='bill')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Save.objects.create(owner=bill, story=story)
        response = self.client.get('/saves/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_saves_story(self):
        self.client.login(username='bill', password='pass')
        bob = User.objects.get(username='bob')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        response = self.client.post('/saves/', {'story': 1})
        count = Save.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_not_logged_in_cant_save_story(self):
        response = self.client.post('/saves/', {'story': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SaveDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Save.objects.create(
            owner=bill, story=story
        )


    def test_can_retrieve_save_using_valid_id(self):
        response = self.client.get('/saves/1/')
        self.assertEqual(response.data['story'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_saves_using_invalid_id(self):
        response = self.client.get('/saves/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unsave_story(self):
        self.client.login(username='bob', password='pass')
        url = reversed('/saves/1/')
        data = {'story': 1}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
