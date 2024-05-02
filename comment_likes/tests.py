from rest_framework import status
from rest_framework.test import APITestCase
from stories.models import Story
from comments.models import Comment
from .models import CommentLike
from django.contrib.auth.models import User


class CommentLikeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')
        User.objects.create_user(username='bill', password='pass')
        User.objects.create_user(username='blake', password='pass')

    def test_can_list_comment_likes(self):
        bob = User.objects.get(username='bob')
        bill = User.objects.get(username='bill')
        blake= User.objects.get(username='blake')
        story = Story.objects.create(owner=bill, title='a title')
        comment = Comment.objects.create(owner=bob, story=story, content='a comment')
        CommentLike.objects.create(owner=blake, comment=comment)
        response = self.client.get('/comment_likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_comment(self):
        self.client.login(username='bob', password='pass')
        bill = User.objects.get(username='bill')
        blake = User.objects.get(username='blake')
        story = Story.objects.create(
            owner=bill, title='a title', content='bills content', description='bills description'
        )
        comment = Comment.objects.create(
            owner=blake, story=story, content='a comment'
        )
        response = self.client.post('/comment_likes/', {'comment': 1})
        count = CommentLike.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_not_logged_in_cant_like_comment(self):
        response = self.client.post('/comment_likes/', {'comment': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentLikeDetailViewTests(APITestCase):
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
        CommentLike.objects.create(
            owner=blake, comment=comment
        )


    def test_can_retrieve_comment_like_using_valid_id(self):
        response = self.client.get('/comment_likes/1/')
        self.assertEqual(response.data['comment'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_likes_using_invalid_id(self):
        response = self.client.get('/comment_likes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unlike_comment(self):
        self.client.login(username='blake', password='pass')
        url = reversed('/comment_likes/1/')
        data = {'comment': 1}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
