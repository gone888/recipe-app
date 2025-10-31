from django.urls import path
<<<<<<< HEAD
from .views import home, RecipeListView, RecipeDetailView

app_name = "recipes"

urlpatterns = [
  path("", home),
  path("list/", RecipeListView.as_view(), name="list"),
  path("list/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
=======
from .views import home

app_name = 'recipes'

urlpatterns = [
  path('', home,),
>>>>>>> a6f8d9918acefca0ce0ea7ef0ac98dcc43889b50
]