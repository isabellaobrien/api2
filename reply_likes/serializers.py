from .models import ReplyLike
from rest_framework import serializers
from django.db import IntegrityError

class ReplyLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReplyLike
        fields = [
            'id', 'owner', 'created_at', 'reply'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate like'
            })