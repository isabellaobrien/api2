from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Follower
from .serializers import FollowerSerializer
from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly 


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
