from rest_framework import status
from rest_framework.test import APITestCase
from stories.models import Story
from .models import Like
from django.contrib.auth.models import User


class LikeListViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')

    def test_can_list_likes(self):
        bob = User.objects.get(username='bob')
        bill = User.objects.get(username='bill')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Like.objects.create(owner=bill, story=story)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_story(self):
        self.client.login(username='bill', password='pass')
        bob = User.objects.get(username='bob')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        response = self.client.post('/likes/', {'story': 1})
        count = Like.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_not_logged_in_cant_like_story(self):
        response = self.client.post('/likes/', {'story': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Like.objects.create(
            owner=bill, story=story
        )


    def test_can_retrieve_like_using_valid_id(self):
        response = self.client.get('/likes/1/')
        self.assertEqual(response.data['story'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_likes_using_invalid_id(self):
        response = self.client.get('/likes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unlike_story(self):
        self.client.login(username='bob', password='pass')
        url = reversed('/likes/1/')
        data = {'story': 1}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
