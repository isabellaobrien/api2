from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from rest_framework import generics, permissions, filters
from social.permissions import IsOwnerOrReadOnly 
from django.db.models import Count


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        comment_likes_count = Count('commentlike', distinct=True),
        comment_reply_count = Count('reply', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comment_likes_count',
        'comment_reply_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        comment_likes_count = Count('commentlike', distinct=True),
        comment_reply_count = Count('reply', distinct=True)
    ).order_by('-created_at')
