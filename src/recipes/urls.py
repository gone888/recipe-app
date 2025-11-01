from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, add_recipe, about_me, get_queryset

app_name = "recipes"

urlpatterns = [
  path("", home, name="home"),
  path('search/', get_queryset, name="search"),
  path("add/", add_recipe, name="add"),
  path("about/", about_me, name="about"),
  path("list/", RecipeListView.as_view(), name="list"),
  path("list/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
]