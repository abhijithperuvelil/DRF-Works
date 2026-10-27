from typing import Any

from rest_framework import serializers
from app.models import  Employee
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    mode_choice=(('Male','Male'),('Female','Female'))
    name = serializers.CharField(max_length=30)
    empid = serializers.IntegerField()
    age = serializers.IntegerField()
    place = serializers.CharField(max_length=30)
    gender = serializers.ChoiceField(choices=mode_choice)
    joining_date = serializers.DateField(read_only=True)
    salary = serializers.IntegerField()
    designation = serializers.CharField(max_length=30)
    image=serializers.ImageField()
    #create is called after validation and before saving
    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError("Age Should Be Positive")
        return data
    def create(self,validated_data):
        e=Employee.objects.create(**validated_data)
        return e
    def update(self,instance,validated_data):
        instance.empid=validated_data.get('empid')
        instance.name=validated_data.get('name')
        instance.age=validated_data.get('age')
        instance.place=validated_data.get('place')
        instance.gender=validated_data.get('gender')
        instance.salary=validated_data.get('salary')
        instance.designation=validated_data.get('designation')
        instance.save()
        return instance
