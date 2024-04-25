from .models import Reply
from rest_framework import serializers

class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Reply
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'content', 'created_at', 'updated_at', 'is_owner', 'comment'
        ]

class ReplyDetailSerializer(ReplySerializer):
    comment = serializers.ReadOnlyField(source='comment.id')