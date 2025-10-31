from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.recipe = Recipe.objects.create(
      name='Test Recipe',
      ingredients='Ingredient1,Ingredient2,Ingredient3',
      cooking_time=30,
      difficulty='Easy',
    )
    
  def test_recipe_creation(self):
    self.assertTrue(isinstance(self.recipe, Recipe))
    self.assertEqual(self.recipe.__str__(), self.recipe.name)
    
  def test_name_max_length(self):
    max_length = self.recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 50)
    
  def test_recipe_name(self):
    recipe_name_label = self.recipe._meta.get_field('name').verbose_name
    self.assertEqual(recipe_name_label, 'name')
    
  def test_difficulty_max_length(self):
    max_length = self.recipe._meta.get_field('difficulty').max_length
    self.assertEqual(max_length, 20)

  def test_string_representation(self):
    self.assertEqual(str(self.recipe), self.recipe.name)
    
  def test_return_ingredients_as_list(self):
    ingredients_list = self.recipe.return_ingredients_as_list()
    self.assertEqual(len(ingredients_list), 3)
    
  def test_calculate_difficulty(self):
    self.recipe.cooking_time = 5
    self.recipe.ingredients = 'Ingredient1,Ingredient2'
    self.recipe.save()
    self.assertEqual(self.recipe.difficulty, 'Easy')
        
  def test_save_method_override(self):
    self.recipe.cooking_time = 20
    self.recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3'
    self.recipe.save()
    self.assertEqual(self.recipe.difficulty, 'Intermediate')
    
  def test_default_image_path(self):
    self.assertEqual(self.recipe.pic, 'No_image_available.png')

class RecipeViewsTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.recipe = Recipe.objects.create(
      name='View Test Recipe',
      ingredients='Ingredient1,Ingredient2,Ingredient3',
      cooking_time=20,
      difficulty='Medium',
    )
    
  def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    
  def test_recipe_list_view(self):
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'View Test Recipe')
    
  def test_recipe_detail_view(self):
    response = self.client.get(reverse('recipes:detail', args=[self.recipe.pk]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'View Test Recipe')