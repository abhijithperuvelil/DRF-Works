from django.db import models

# Create your models here.
class Employee(models.Model):
    mode_choice=(('Male','Male'),('Female','Female'))
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,choices=mode_choice)
    joining_date=models.DateField(auto_now_add=True)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    image=models.ImageField()





