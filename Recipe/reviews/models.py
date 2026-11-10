from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
from recipes.models import RecipeModel

# Create your models here.
class ReviewModel(models.Model):
    recipe=models.ForeignKey(RecipeModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)