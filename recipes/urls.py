from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, recipe_search, add_recipe, about_me

app_name = "recipes"

urlpatterns = [
  path('homescreen', home, name='home'),
  path("search/", recipe_search, name="search"),
  path("add/", add_recipe, name="add"),
  path("about/", about_me, name="about"),
  path("list/", RecipeListView.as_view(), name="list"),
  path("list/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
]