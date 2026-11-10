from django.db import models

# Create your models here.
class RecipeModel(models.Model):
    recipe_name=models.CharField(max_length=30)
    ingredients=models.CharField(max_length=30)
    instructions=models.TextField(max_length=30)
    mealtype=models.CharField(max_length=30)
    cuisine=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images',null=True,blank=True)