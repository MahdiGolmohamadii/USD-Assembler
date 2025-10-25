import sys
from PyQt6 import QtWidgets


class FileBrowser(QtWidgets.QDialog):
    def __init__(self, parent, stage):
        super().__init__(parent)
        self.stage = stage
        self.create_widgets()
        self.create_layout()
        self.create_connections()


    def create_widgets(self):
        self.tree_widget = QtWidgets.QTreeWidget()
        # self.tree_widget.setColumnCount(5)

        # items = []
        # for i in range(16):
        #     items.append(QtWidgets.QTreeWidgetItem())

        # child = []
        # for i in range(3):
        #     child.append(QtWidgets.QTreeWidgetItem(items[0]))
        # self.tree_widget.insertTopLevelItems(0, items)
        # self.populate_tree(self.stage)
        for p in self.stage.Traverse():
            self.populate_tree(p, self.tree_widget)
        
        
        

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.tree_widget)
    def create_connections(self):
        pass


    def populate_tree(self, prim, parent_widget, parent_item=None):
        if parent_item is None:
            parent_item = parent_widget.invisibleRootItem()

        for child in prim.GetChildren():
            item = QtWidgets.QTreeWidgetItem([child.GetName(), child.GetTypeName()])
            parent_item.addChild(item)
            self.populate_tree(child, parent_widget, item)