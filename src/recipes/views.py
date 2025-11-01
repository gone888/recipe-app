from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeSearchForm, RecipeForm
import pandas as pd
from .utils import get_chart, get_recipename_from_id

# Create your views here.
def home(request):
  return render(request, "recipes/recipes_home.html")

def recipe_search(request):
  form = RecipeSearchForm(request.POST or None)
  recipe_df = None
  chart = None

  if request.method == 'POST':
    recipe_title = request.POST.get('recipe_title')
    chart_type = request.POST.get('chart_type')
    qs = Recipe.objects.filter(name=recipe_title)
    if qs:
      recipe_df = pd.DataFrame(qs.values())
      recipe_df['id'] = recipe_df['id'].apply(get_recipename_from_id)
      chart = get_chart(chart_type, recipe_df, labels=recipe_df['difficulty'].values)
      recipe_df = recipe_df.to_html()

  context = {
    'form': form,
    'recipe_df': recipe_df,
    'chart': chart,
  }
  return render(request, 'recipes/recipe_search.html', context)

def add_recipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('recipes:home')  # Redirect to a page where recipes are listed
  else:
    form = RecipeForm()
    
  return render(request, 'recipes/add_recipe.html', {'form': form})

def about_me(request):
  return render(request, 'recipes/about_me.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = "recipes/recipe_list.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = "recipes/recipe_details.html"
