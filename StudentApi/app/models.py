from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Course=models.CharField(max_length=30)
    Marks=models.IntegerField()
# class Course(models.Model):
#     # db value,display value for choice
#     mode_choice=(('Online','ONLINE'),('Offline','OFFLINE'))
#     Course_Name=models.CharField(max_length=30)
#     Fee=models.IntegerField()
#     Duration=models.CharField(max_length=10)
#     Instructor=models.CharField(max_length=30)
#     Mode=models.CharField(choices=mode_choice)
