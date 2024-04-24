from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Story
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'content', 'description'
        ]

