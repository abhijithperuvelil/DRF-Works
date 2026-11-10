from django.db import models
from doctor.models import Doctor
# Create your models here.
class AppointmentModel(models.Model):
    choice=(('male','Male'),('female','Female'))
    patient_name=models.CharField(max_length=30,null=True)
    age=models.IntegerField()
    gender=models.CharField(choices=choice,max_length=30)
    phone=models.CharField(max_length=30)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE) # to avoid redundancy of data
    problem=models.TextField()
    appointment_date=models.DateField()
    appoint_time=models.TimeField(null=True)
    token_number=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
