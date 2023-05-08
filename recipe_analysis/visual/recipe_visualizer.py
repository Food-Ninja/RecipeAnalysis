import sys
import recipe_analysis.analysis as ana
from enum import Enum
from typing import List
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMainWindow, \
     QComboBox
from .recipe_table import RecipeTableView
from ..model import Recipe


class DropDownItems(Enum):
    DEFAULT = 'Search only'
    ANATOMY_BIGRAM = 'Analyse anatomy (Bigram)'
    ANATOMY_2_STEP = 'Analyse anatomy (2-Step)'
    COLOUR_BIGRAM = 'Analyse colour (Bigram)'
    COLOUR_2_STEP = 'Analyse colour (2-Step)'


class RecipeVisualizer(QMainWindow):
    def __init__(self, recipes: List[Recipe], parent=None):
        super().__init__(parent)
        self.setWindowTitle('Recipe1M+ Analysis')
        self.__recipes = recipes
        self.__last_search = ''
        self.central = QWidget()
        self.search = QLineEdit()
        self.search_alg = QComboBox()
        self.search_alg.addItems([i.value for i in DropDownItems])
        self.search_btn = QPushButton('Search')
        self.search_btn.clicked.connect(self.start_search)
        self.table = RecipeTableView(recipes, 0, 2)
        self.set_content()

    def set_content(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.search)
        h_layout.addWidget(self.search_alg)
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
        if search_text != self.__last_search:
            for r in self.__recipes:
                r.reset_filter()
                r.filter_complete(search_text)
            self.table.update_data(self.__recipes)
            self.__last_search = search_text
        txt = self.search_alg.currentText()
        if txt != DropDownItems.DEFAULT.value:
            if txt == DropDownItems.ANATOMY_2_STEP.value or txt == DropDownItems.ANATOMY_BIGRAM.value:
                ana.search_and_print_anatomical_parts(self.__recipes, search_text, txt == DropDownItems.ANATOMY_BIGRAM.value)
            if txt == DropDownItems.COLOUR_2_STEP.value or txt == DropDownItems.COLOUR_BIGRAM.value:
                ana.search_and_print_colours(self.__recipes, search_text, txt == DropDownItems.COLOUR_BIGRAM.value)


def visualize_recipes(recipes: List[Recipe]):
    print('\nPreparing the visualization...')
    app = QApplication(sys.argv)
    window = RecipeVisualizer(recipes)
    window.showMaximized()
    sys.exit(app.exec_())
