import recipe_analysis.io as ra_io

recipes = ra_io.read_recipes()
ra_io.visualize_recipes(recipes)
