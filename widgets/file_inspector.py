import sys
from PyQt6 import QtWidgets, QtCore
from widgets.attributes import Attributes


class FileInspector(QtWidgets.QDialog):
    def __init__(self, parent, stage):
        super().__init__(parent)
        self.stage = stage

        self.setMinimumSize(300,200)
        self.setWindowTitle(self.stage.GetRootLayer().identifier)

        self.create_widgets()
        self.create_layout()
        self.create_connections()


    def create_widgets(self):
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setColumnCount(3)
        for p in self.stage.Traverse():
            self.populate_tree(p, self.tree_widget)
        self.tree_widget.resizeColumnToContents(0)
        
        

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.tree_widget)
    def create_connections(self):
        self.tree_widget.itemClicked.connect(self.on_cell_clicked)


    def populate_tree(self, prim, parent_widget, parent_item=None):
        if parent_item is None:
            parent_item = parent_widget.invisibleRootItem()

        for child in prim.GetChildren():
            item = QtWidgets.QTreeWidgetItem([child.GetName(), child.GetTypeName()])
            item.setData(0, QtCore.Qt.ItemDataRole.UserRole, str(child.GetPath()))
            parent_item.addChild(item)
            self.populate_tree(child, parent_widget, item)

    
    def on_cell_clicked(self, item, column):
        prim_path = item.data(0, QtCore.Qt.ItemDataRole.UserRole)

        if prim_path:
            prim = self.stage.GetPrimAtPath(prim_path)
        if prim:
            self.attrib_window = Attributes(self, prim)
            self.attrib_window.show()