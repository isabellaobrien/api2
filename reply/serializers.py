from .models import Reply
from reply_likes.models import ReplyLike
from rest_framework import serializers

class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reply_like_id = serializers.SerializerMethodField()
    reply_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_reply_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reply_like = ReplyLike.objects.filter(
                 owner=user, reply=obj
            ).first()
            return reply_like.id if reply_like else None
        return None

    class Meta:
        model = Reply
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'content', 'created_at', 'updated_at', 'is_owner', 'comment',
            'reply_like_id', 'reply_likes_count'
        ]

class ReplyDetailSerializer(ReplySerializer):
    comment = serializers.ReadOnlyField(source='comment.id')