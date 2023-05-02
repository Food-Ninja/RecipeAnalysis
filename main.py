import recipe_analysis.io as ra_io
import sys

recipes = ra_io.read_recipes()
ra_io.visualize_recipes(sys.argv, recipes)
