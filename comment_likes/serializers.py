from .models import CommentLike
from rest_framework import serializers
from django.db import IntegrityError

class CommentLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = [
            'id', 'owner', 'created_at', 'comment'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate like'
            })