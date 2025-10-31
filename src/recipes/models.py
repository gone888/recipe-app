from django.db import models

# Create your models here.

class Recipe(models.Model):
  name = models.CharField(max_length=120)
  ingredients = models.TextField(default='No ingredients')
  cooking_time = models.IntegerField()
  difficulty = models.CharField(max_length=20, blank=True, null=True)

  def calculate_difficulty(self):
    num_ingredients = len(self.return_ingredients_as_list())
    if self.cooking_time < 10 and num_ingredients < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and num_ingredients >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and num_ingredients < 4:
      self.difficulty = "Intermediate"
    else:
      self.difficulty = "Hard"
    self.save()

  def __str__(self):
    return str(self.name)