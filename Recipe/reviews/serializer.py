from rest_framework import serializers

from reviews.models import ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReviewModel
        fields='__all__'
        read_ony_fields=['user','created_at']
