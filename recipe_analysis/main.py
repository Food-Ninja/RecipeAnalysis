from recipe_analysis.data_import import read_recipes
from recipe_analysis.visual import visualize_recipes

recipes = read_recipes()
visualize_recipes(recipes)
