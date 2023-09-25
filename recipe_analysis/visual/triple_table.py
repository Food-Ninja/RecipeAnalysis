from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from typing import List


class TripleTableView(QTableWidget):
    HEADERS = ('Subject', 'Relation', 'Object')

    def __init__(self, data: List[dict], *args):
        QTableWidget.__init__(self, *args)
        self.__data = data
        self.set_content()
        self.setWordWrap(True)
        self.resizeColumnsToContents()
        # TODO: resize each individual row to fit the whole list of steps (self.resizeRowsToContents() does not help)

    def set_content(self):
        self.clearContents()
        self.setRowCount(len(self.__data))
        count = 0

        for t in self.__data:
            subj = QTableWidgetItem(t['subject'])
            rel = QTableWidgetItem(t['relation'])
            obj = QTableWidgetItem(t['object'])
            self.setItem(count, 0, subj)
            self.setItem(count, 1, rel)
            self.setItem(count, 2, obj)
            count += 1
        self.setHorizontalHeaderLabels(self.HEADERS)

    def update_data(self, data: List[dict]):
        self.__data = data
        self.set_content()

    def resizeColumnsToContents(self):
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
