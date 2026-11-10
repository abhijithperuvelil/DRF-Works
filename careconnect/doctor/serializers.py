from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self, validated_data):
        a=User.objects.create_superuser(**validated_data)
        a.save()
        return a