from django.db import models

# Create your models here.
class Doctor(models.Model):
    choice=(
    ("cardiology", "Cardiology"),
    ("dermatology", "Dermatology"),
    ("endocrinology", "Endocrinology"),
    ("ent", "Ear, Nose & Throat (ENT)"),
    ("gastroenterology", "Gastroenterology"),
    ("general medicine", "General Medicine / Internal Medicine"),
    ("general_surgery", "General Surgery"),
    ("gynecology", "Gynecology & Obstetrics"),
    ("hematology", "Hematology"),
    ("nephrology", "Nephrology"),
    ("neurology", "Neurology"),
    ("oncology", "Oncology"),
    ("ophthalmology", "Ophthalmology"),
    ("orthopedics", "Orthopedics"),
    ("pediatrics", "Pediatrics"),
    ("psychiatry", "Psychiatry"),
    ("pulmonology", "Pulmonology"),
    ("radiology", "Radiology"),
    ("urology", "Urology"),
    ("other", "Other"))
    name=models.CharField(max_length=30,null=True)
    specialization=models.CharField(max_length=30,choices=choice,null=True)
    fee=models.IntegerField()
    qualification=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
