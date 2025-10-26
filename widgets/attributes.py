from PyQt6 import QtWidgets, QtCore


class Attributes(QtWidgets.QDialog):
    def __init__(self, parent, prim):
        super().__init__(parent)
        self.prim = prim
        
        self.populate_attrib_table(prim)

        self.setWindowTitle(str(prim.GetPath()))
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.attrib_table = QtWidgets.QTableWidget()
        self.attrib_table.setColumnCount(5)
        self.attrib_table.setRowCount(10)
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.attrib_table)
    def create_connections(self):
        pass


    def populate_attrib_table(self, prim):
        for attr in prim.GetAttributes():
            print(attr.Get())
            print(attr.GetName())