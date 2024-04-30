from rest_framework import status
from rest_framework.test import APITestCase
from .models import Story
from django.contrib.auth.models import User


class StoryListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')

    def test_can_list_stories(self):
        bob = User.objects.get(username='bob')
        Story.objects.create(owner=bob, title='a title')
        response = self.client.get('/stories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_story(self):
        self.client.login(username='bob', password='pass')
        response = self.client.post('/stories/', {'title': 'a title','description': 'a description', 'content': 'some content'})
        count = Story.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_story(self):
        response = self.client.post('/stories/', {'title': 'a title','description': 'a description', 'content': 'some content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StoryDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')
        Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Story.objects.create(
            owner=bill, title='another title', content='bills content', description='bills description'
        )

    def test_can_retrieve_story_using_valid_id(self):
        response = self.client.get('/stories/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_story_using_invalid_id(self):
        response = self.client.get('/stories/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_story(self):
        self.client.login(username='bob', password='pass')
        response = self.client.put('/stories/1/', {'title': 'a new title', 'content':'bobs content', 'description':'bobs description'})
        story = Story.objects.filter(pk=1).first()
        self.assertEqual(story.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_story(self):
        self.client.login(username='bob', password='pass')
        response = self.client.put('/stories/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)