from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer
from rest_framework import generics, permissions, filters
from social.permissions import IsOwnerOrReadOnly 
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class StoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StorySerializer
    queryset = Story.objects.annotate(
        likes_count = Count('like', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'like__created_at',
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'like__owner__profile',
        'owner__profile',
    ]

    def perform_create(self, serializer):
        print("Authenticated User:", self.request.user)
        serializer.save(owner=self.request.user)

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StorySerializer
    # queryset = Story.objects.all()
    queryset = Story.objects.annotate(
        likes_count = Count('like', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_at')