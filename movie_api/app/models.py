from django.db import models
from rest_framework.fields import CharField


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    rating=models.IntegerField()
    runtime=models.IntegerField()
    image=models.ImageField(upload_to="movies",null=True,blank=True)

