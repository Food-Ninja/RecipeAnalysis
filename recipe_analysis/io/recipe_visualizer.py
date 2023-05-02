import sys
from PyQt5.QtWidgets import QApplication
from .recipe_table import RecipeTableView


def visualize_recipes(args, recipes):
    app = QApplication(args)
    print('\nPreparing the visualization...')
    table = RecipeTableView(recipes, len(recipes), 2)
    table.showMaximized()
    sys.exit(app.exec_())
