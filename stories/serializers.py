from rest_framework import serializers
from .models import Story
from likes.models import Like

class StorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                 owner=user, story=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Story
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'content', 'description', 'is_owner', 'profile_id',
            'profile_image', 'like_id', 'likes_count', 'comments_count'
        ]

