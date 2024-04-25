from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer
from rest_framework import generics, permissions, filters
from social.permissions import IsOwnerOrReadOnly 
from django.db.models import Count


class StoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StorySerializer
    # queryset = Story.objects.all()
    queryset = Story.objects.annotate(
        likes_count = Count('like', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StorySerializer
    # queryset = Story.objects.all()
    queryset = Story.objects.annotate(
        likes_count = Count('like', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_at')