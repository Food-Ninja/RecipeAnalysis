import sys
from typing import List
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMainWindow
from .recipe_table import RecipeTableView
from ..model import Recipe


class RecipeVisualizer(QMainWindow):
    def __init__(self, recipes: List[Recipe], parent=None):
        super().__init__(parent)
        self.setWindowTitle('Recipe1M+ Analysis')
        self.__recipes = recipes
        self.central = QWidget()
        self.search = QLineEdit()
        self.search_btn = QPushButton('Search')
        self.search_btn.clicked.connect(self.start_search)
        self.table = RecipeTableView(recipes, 0, 2)
        self.set_content()

    def set_content(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.search)
        h_layout.addWidget(self.search_btn)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.table)

        self.central.setLayout(v_layout)
        self.setCentralWidget(self.central)

    def start_search(self):
        search_text = self.search.text()
        if not search_text:
            return
        # TODO: Add progress bar (or anything to keep GUI responsive)
        for r in self.__recipes:
            r.reset_filter()
            r.filter_complete(search_text)
        self.table.update_data(self.__recipes)


def visualize_recipes(recipes: List[Recipe]):
    print('\nPreparing the visualization...')
    app = QApplication(sys.argv)
    window = RecipeVisualizer(recipes)
    window.showMaximized()
    sys.exit(app.exec_())
