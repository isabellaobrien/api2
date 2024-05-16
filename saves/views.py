from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Save
from .serializers import SaveSerializer
from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly 


class SaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SaveDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
