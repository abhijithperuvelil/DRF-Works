from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=30)
    Age = serializers.IntegerField()
    Course = serializers.CharField(max_length=30)
    Marks = serializers.IntegerField()
    def create(self, validated_data):
        s = Student.objects.create(**validated_data)
        return s
    def update(self,instance,validate_data):
        instance.Name=validate_data.get('Name')
        instance.Age=validate_data.get('Age')
        instance.Course=validate_data.get('Course')
        instance.Marks=validate_data.get('Marks')
        return instance