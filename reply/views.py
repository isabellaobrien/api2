from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer
from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly 


class ReplyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyDetailSerializer
    queryset = Reply.objects.all()