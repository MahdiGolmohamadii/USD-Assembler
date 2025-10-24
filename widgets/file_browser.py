import sys
from PyQt6 import QtWidgets


class FileBrowser(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()


    def create_widgets(self):
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setColumnCount(5)

        items = []
        for i in range(16):
            items.append(QtWidgets.QTreeWidgetItem())

        child = []
        for i in range(3):
            child.append(QtWidgets.QTreeWidgetItem(items[0]))
        self.tree_widget.insertTopLevelItems(0, items)
        
        
        

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.tree_widget)
    def create_connections(self):
        pass