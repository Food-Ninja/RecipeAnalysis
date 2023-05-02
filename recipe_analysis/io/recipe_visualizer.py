import sys
from typing import List
from PyQt5.QtWidgets import QApplication
from .recipe_table import RecipeTableView
from recipe_analysis.model.recipe import Recipe


def visualize_recipes(args, recipes: List[Recipe]):
    app = QApplication(args)
    print('\nPreparing the visualization...')
    table = RecipeTableView(recipes, count_visible_recipes(recipes), 2)
    table.showMaximized()
    sys.exit(app.exec_())


def count_visible_recipes(recipes: List[Recipe]):
    count = 0
    for r in recipes:
        if r.is_visible():
            count = count + 1
    return count
