from django.db import models as M

# Create your models here.
class Employee(M.Model):
    mode_choice=(('Male','Male'),('Female','Female'))
    name = M.CharField(max_length=30)
    empid = M.IntegerField()
    age = M.IntegerField()
    place = M.CharField(max_length=30)
    gender = M.CharField(max_length=10, choices=mode_choice)
    joining_date = M.DateField(auto_now_add=True)
    salary = M.IntegerField()
    designation = M.CharField(max_length=30)
    image=M.ImageField(upload_to="image",null=True,blank=True)

