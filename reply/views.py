from rest_framework.views import APIView
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer
from rest_framework import generics, permissions, filters
from social.permissions import IsOwnerOrReadOnly 
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class ReplyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplySerializer
    queryset = Reply.objects.annotate(
        reply_likes_count=Count('replylike', distinct=True),
    ).order_by('-created_at')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    
    filterset_fields = [
        'comment',
        # 'reply_likes_count'
    ]
    

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyDetailSerializer
    queryset = Reply.objects.annotate(
        reply_likes_count=Count('replylike', distinct=True),
    ).order_by('-created_at')
