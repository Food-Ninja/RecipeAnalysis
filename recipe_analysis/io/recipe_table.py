from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from typing import List
from ..model import Recipe


class RecipeTableView(QTableWidget):
    HEADERS = ('Recipe Title', 'Steps')

    def __init__(self, data: List[Recipe], *args):
        QTableWidget.__init__(self, *args)
        self.__data = data
        self.set_content()
        self.setWordWrap(True)
        self.resizeColumnsToContents()
        # TODO: resize each individual row to fit the whole list of steps (self.resizeRowsToContents() does not help)

    def set_content(self):
        self.clearContents()
        rows = self.count_visible_recipes()
        self.setRowCount(rows)
        count = 0

        for r in self.__data:
            if not isinstance(r, Recipe) or not r.is_visible():
                continue
            title = QTableWidgetItem(r.get_title())
            steps = QTableWidgetItem(r.get_steps_as_single_string())
            self.setItem(count, 0, title)
            self.setItem(count, 1, steps)
            count += 1
        self.setHorizontalHeaderLabels(self.HEADERS)

    def update_data(self, data: List[Recipe]):
        self.__data = data
        self.set_content()

    def resizeColumnsToContents(self):
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

    def count_visible_recipes(self) -> int:
        count = 0
        for r in self.__data:
            if r.is_visible():
                count += 1
        return count
