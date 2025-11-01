from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, RecipeForm
import pandas as pd
from .utils import get_chart

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes_home.html')

@login_required
def get_queryset(request):
    form = RecipeSearchForm(request.POST or None)
    # Initialize dataframe
    recipes_df = None
    qs = None
    chart = None

    if request.method == 'POST':
      recipe_search = request.POST.get('recipe_search')
      chart_type = request.POST.get('chart_type')

      qs = Recipe.objects.filter(
          Q(name__icontains=recipe_search) |
          Q(ingredients__icontains=recipe_search) |
          Q(name=recipe_search)
        )

      if qs:
        recipes_df = pd.DataFrame(qs.values())

        chart = get_chart(chart_type, recipes_df, recipe_search)

        #convert the dataframe to HTML
        recipes_df=recipes_df.to_html()

      else:
        qs = 'No recipes found'

    context = {
      'form': form,
      'recipes_df': recipes_df,
      'qs': qs,
      'chart': chart}

    return render(request, 'recipes/recipe_search.html', context)

@login_required
def add_recipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      messages.info(request, 'Recipe added successfully!')
      return redirect('recipes:list')
  else:
    form = RecipeForm()

  return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def about_me(request):
    return render(request, 'recipes/about_me.html')

@login_required
def update_recipe(request, pk):
    # Retrieve the recipe or return a 404 if not found
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.info(request, 'Recipe updated successfully!')
            return redirect('recipes:details', recipe.pk)
    else:
        # If not a POST request, instantiate the form with the existing recipe
        form = RecipeForm(instance=recipe)
    # Render the template with the form and recipe instance
    return render(request, 'recipes/recipe_details.html', {'form': form, 'object': recipe})

@login_required
def delete_recipe(request, pk):
  recipe = get_object_or_404(Recipe, pk=pk)
  recipe.delete()
  messages.info(request, 'Recipe deleted successfully!')
  return redirect('recipes:list')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/recipe_details.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) # Adds extra information to the context passed to the template.
      
      recipe = self.get_object() # Retrieves the specific Recipe object being viewed.
      context['form'] = RecipeForm(instance=recipe)  # Adds a form populated with the recipe's data to the context.
      return context