import sys
import recipe_analysis.analysis as ana
from enum import Enum
from typing import List
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMainWindow, \
     QComboBox, QStackedWidget
from .recipe_table import RecipeTableView
from .triple_table import TripleTableView
from ..model import Recipe


class DropDownItems(Enum):
    DEFAULT = 'Search only'
    ANATOMY_BIGRAM = 'Analyse anatomy (Bigram)'
    ANATOMY_2_STEP = 'Analyse anatomy (2-Step)'
    COLOUR_BIGRAM = 'Analyse colour (Bigram)'
    COLOUR_2_STEP = 'Analyse colour (2-Step)'
    TOOL_BIGRAM = 'Analyse removal tool (Bigram)'
    TOOL_2_STEP = 'Analyse removal tool (2-step)'
    EDIBILITY_BIGRAM = 'Analyse edibility (Bigram)'
    EDIBILITY_2_STEP = 'Analyse edibility (2-step)'
    OPENIE = 'Triple Extraction (OpenIE)'
    FRU_AND_VEG = 'Count Fruits & Vegetables'


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
        self.widget_stack = QStackedWidget(self)
        self.rec_table_widget = QWidget()
        self.trip_table_widget = QWidget()
        self.rec_table = RecipeTableView(recipes, 0, 2)
        self.trip_table = TripleTableView([], 0, 3)
        self.set_content()

    def set_content(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.search)
        h_layout.addWidget(self.search_alg)
        h_layout.addWidget(self.search_btn)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.widget_stack)

        rec_table_layout = QHBoxLayout()
        rec_table_layout.addWidget(self.rec_table)
        self.rec_table_widget.setLayout(rec_table_layout)
        self.widget_stack.addWidget(self.rec_table_widget)
        self.widget_stack.setCurrentWidget(self.rec_table_widget)

        trip_table_layout = QHBoxLayout()
        trip_table_layout.addWidget(self.trip_table)
        self.trip_table_widget.setLayout(trip_table_layout)
        self.widget_stack.addWidget(self.trip_table_widget)

        self.central.setLayout(v_layout)
        self.setCentralWidget(self.central)

    def start_search(self):
        search_type = self.search_alg.currentText()
        if search_type == DropDownItems.FRU_AND_VEG.value:
            ana.count_fruit_and_veggie_occurrences(self.__recipes)
            return

        search_text = self.search.text()
        if not search_text:
            return

        # TODO: Add progress bar (or anything to keep GUI responsive)
        if search_text != self.__last_search:
            for r in self.__recipes:
                r.reset_filter()
                r.filter_complete(search_text)
            self.rec_table.update_data(self.__recipes)
            self.__last_search = search_text

        if search_type == DropDownItems.DEFAULT.value:
            self.widget_stack.setCurrentWidget(self.rec_table_widget)
        if search_type == DropDownItems.ANATOMY_2_STEP.value or search_type == DropDownItems.ANATOMY_BIGRAM.value:
            ana.search_and_print_anatomical_parts(self.__recipes, search_text, search_type == DropDownItems.ANATOMY_BIGRAM.value)
            self.widget_stack.setCurrentWidget(self.rec_table_widget)
        if search_type == DropDownItems.COLOUR_2_STEP.value or search_type == DropDownItems.COLOUR_BIGRAM.value:
            ana.search_and_print_colours(self.__recipes, search_text, search_type == DropDownItems.COLOUR_BIGRAM.value)
            self.widget_stack.setCurrentWidget(self.rec_table_widget)
        if search_type == DropDownItems.TOOL_2_STEP.value or search_type == DropDownItems.TOOL_BIGRAM.value:
            ana.search_and_print_removal_tool(self.__recipes, search_text, search_type == DropDownItems.TOOL_BIGRAM.value)
            self.widget_stack.setCurrentWidget(self.rec_table_widget)
        if search_type == DropDownItems.EDIBILITY_2_STEP.value or search_type == DropDownItems.EDIBILITY_BIGRAM.value:
            ana.search_and_print_edibility(self.__recipes, search_text, search_type == DropDownItems.EDIBILITY_BIGRAM.value)
            self.widget_stack.setCurrentWidget(self.rec_table_widget)
        if search_type == DropDownItems.OPENIE.value:
            triples = ana.extract_triples(self.__recipes, search_text)
            self.trip_table.update_data(triples)
            self.widget_stack.setCurrentWidget(self.trip_table_widget)


def visualize_recipes(recipes: List[Recipe]):
    print('\nPreparing the visualization...')
    app = QApplication(sys.argv)
    window = RecipeVisualizer(recipes)
    window.showMaximized()
    sys.exit(app.exec_())
