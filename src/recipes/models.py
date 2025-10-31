from django.db import models

# Create your models here.

class Recipe(models.Model):
  name = models.CharField(max_length=120)
  ingredients = models.TextField(default='No ingredients')
  cooking_time = models.IntegerField()

  def __str__(self):
    return str(self.name)