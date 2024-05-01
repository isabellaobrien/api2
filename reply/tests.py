from rest_framework import status
from rest_framework.test import APITestCase
from .models import Reply
from comments.models import Comment
from stories.models import Story
from django.contrib.auth.models import User


class ReplyListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')
        User.objects.create_user(username='blake', password='pass')

    def test_can_list_replies(self):
        bob = User.objects.get(username='bob')
        bill = User.objects.get(username='bill')
        blake = User.objects.get(username='blake')
        story = Story.objects.create(owner=bill, title='a title')
        comment = Comment.objects.create(owner=bob, story=story, content='a comment')
        reply = Reply.objects.create(owner=blake, comment=comment, content='a reply')
        response = self.client.get('/replies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_logged_in_user_can_create_reply(self):
        self.client.login(username='bob', password='pass')
        bill = User.objects.get(username='bill')
        blake = User.objects.get(username='blake')
        story = Story.objects.create(
            owner=bill, title='a title', content='bills content', description='bills description'
        )
        comment = Comment.objects.create(
            owner=blake, story=story, content='a comment'
        )
        response = self.client.post('/replies/', {'comment': 1, 'content': 'a reply'})
        count = Reply.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_reply(self):
        response = self.client.post('/replies/', {'comment': 1, 'content': 'a reply'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReplyDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        bill = User.objects.create_user(username='bill', password='pass')
        blake = User.objects.create_user(username='blake', password='pass')
        story = Story.objects.create(
            owner=bob, title='a title', content='bobs content', description='bobs description'
        )
        comment = Comment.objects.create(
            owner=bill, story=story, content="comment content"
        )
        Reply.objects.create(
            owner=blake, comment=comment, content="reply 1"
        )
        Reply.objects.create(
            owner=bob, comment=comment, content="reply 2"
        )

    def test_can_retrieve_reply_using_valid_id(self):
        response = self.client.get('/replies/1/')
        self.assertEqual(response.data['content'], 'reply 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_reply_using_invalid_id(self):
        response = self.client.get('/replies/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_reply(self):
        self.client.login(username='blake', password='pass')
        response = self.client.put('/replies/1/', {'comment': 1, 'content': 'new reply 1'})
        reply = Reply.objects.filter(pk=1).first()
        self.assertEqual(reply.content, 'new reply 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_reply(self):
        self.client.login(username='bill', password='pass')
        response = self.client.put('/replies/2/', {'comment': 1, 'content': 'new reply 2'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

