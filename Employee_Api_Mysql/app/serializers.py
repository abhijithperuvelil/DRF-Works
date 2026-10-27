from typing import Any

from django.db.models.base import Model
from rest_framework import serializers

from app import models
from app.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
    def create(self, validated_data):
        e = Employee.objects.create(**validated_data)
        return e

