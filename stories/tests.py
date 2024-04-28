# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Story
# from django.contrib.auth.models import User


# class StoryListViewTests(APITestCase):
#     def setUp(self):
#         User.objects.create_user(username='adam', password='pass')

#     def test_can_list_stories(self):
#         adam = User.objects.get(username='adam')
#         Story.objects.create(owner=adam, title='a title')
#         response = self.client.get('/stories/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(response.data)
#         print(len(response.data))

#     def test_logged_in_user_can_create_story(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.post('/stories/', {'title': 'a title'})
#         count = Story.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         print(response.data)
#         print(count)

#     def test_user_not_logged_in_cant_create_story(self):
#         response = self.client.post('/stories/', {'title': 'a title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class StoryDetailViewTests(APITestCase):
#     def setUp(self):
#         adam = User.objects.create_user(username='adam', password='pass')
#         brian = User.objects.create_user(username='brian', password='pass')
#         Story.objects.create(
#             owner=adam, title='a title', content='adams content'
#         )
#         Story.objects.create(
#             owner=brian, title='another title', content='brians content'
#         )

#     def test_can_retrieve_story_using_valid_id(self):
#         response = self.client.get('/stories/1/')
#         self.assertEqual(response.data['title'], 'a title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_post_using_invalid_id(self):
#         response = self.client.get('/stories/999/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_own_story(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.put('/stories/1/', {'title': 'a new title'})
#         story = Story.objects.filter(pk=1).first()
#         self.assertEqual(story.title, 'a new title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cant_update_another_users_story(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.put('/stories/2/', {'title': 'a new title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)