from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CommentLike
from .serializers import CommentLikeSerializer
from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly 


class CommentLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
