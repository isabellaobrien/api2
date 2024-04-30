from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from stories.models import Story
from django.contrib.auth.models import User


class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')

    def test_can_list_comments(self):
        bob = User.objects.get(username='bob')
        bill = User.objects.get(username='bill')
        story = Story.objects.create(owner=bill, title='a title')
        Comment.objects.create(owner=bob, story=story, content='a comment')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='bob', password='pass')
        bill = User.objects.get(username='bill')
        story = Story.objects.create(
            owner=bill, title='a title', content='bills content', description='bills description'
        )
        response = self.client.post('/comments/', {'story': 1, 'content': 'some content'})
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_comment(self):
        response = self.client.post('/comments/', {'story': 1, 'content': 'some content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')
        blake = User.objects.create_user(username='blake', password='pass')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        Comment.objects.create(
            owner=bill, story=story, content="comment content"
        )
        Comment.objects.create(
            owner=blake, story=story, content="comment content 2"
        )

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'comment content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/stories/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        self.client.login(username='bill', password='pass')
        response = self.client.put('/comments/1/', {'story': 1, 'content': 'new comment content'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'new comment content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_comment(self):
        self.client.login(username='bill', password='pass')
        response = self.client.put('/comments/2/', {'story': 1, 'content': 'new comment content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
