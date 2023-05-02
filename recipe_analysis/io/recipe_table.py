from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from typing import List
from recipe_analysis.model.recipe import Recipe


class RecipeTableView(QTableWidget):
    def __init__(self, data: List[Recipe], *args):
        QTableWidget.__init__(self, *args)
        self.__data = data
        self.set_data()
        self.setWordWrap(True)
        self.resizeColumnsToContents()
        # TODO: resize each individual row to fit the whole list of steps (self.resizeRowsToContents() does not help)

    def set_data(self):
        headers = ['Recipe Title', 'Steps']
        count = 0
        for r in self.__data:
            if not isinstance(r, Recipe) or not r.is_visible():
                continue
            title = QTableWidgetItem(r.get_title())
            steps = QTableWidgetItem(r.get_steps_as_single_string())
            self.setItem(count, 0, title)
            self.setItem(count, 1, steps)
            count = count+1
        self.setHorizontalHeaderLabels(headers)

    def resizeColumnsToContents(self):
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
