from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer
from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly 


class StoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StorySerializer
    queryset = Story.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StorySerializer
    queryset = Story.objects.all()