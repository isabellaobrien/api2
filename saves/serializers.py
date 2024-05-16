from .models import Save
from rest_framework import serializers
from django.db import IntegrityError

class SaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = [
            'id', 'owner', 'created_at', 'story'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate save'
            })