from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
  def setUpTestData():
    Recipe.objects.create(name='Omelette',
      ingredients='Eggs, Cream, Peppers, Salt, Black Pepper',
      cooking_time=4,
    )
      
  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_ingredients(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('ingredients').verbose_name
    self.assertEqual(field_label, 'ingredients')