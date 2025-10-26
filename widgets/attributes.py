from PyQt6 import QtWidgets, QtCore


class Attributes(QtWidgets.QDialog):
    def __init__(self, parent, prim):
        super().__init__(parent)
        self.prim = prim
        
        

        self.setWindowTitle(str(prim.GetPath()))
        self.create_widgets()
        self.create_layouts()
        self.create_connections()


    def create_widgets(self):
        self.attrib_table = QtWidgets.QTableWidget()
        self.populate_attrib_table(self.prim)
        self.attrib_table.resizeColumnsToContents()
        self.attrib_table.resizeRowsToContents()

        
        
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.attrib_table)
        self.setLayout(main_layout)
        self.adjustSize()
    def create_connections(self):
        pass


    def populate_attrib_table(self, prim):
        attribs = prim.GetAttributes()

        self.attrib_table.clear()
        self.attrib_table.setColumnCount(3)
        self.attrib_table.setHorizontalHeaderLabels(["Name", "Type", "Value"])
        self.attrib_table.setRowCount(len(attribs))

        for i, attr in enumerate(attribs):

            name_item = QtWidgets.QTableWidgetItem(attr.GetName())
            type_item = QtWidgets.QTableWidgetItem(str(attr.GetTypeName()))
            
            val = attr.Get()
            val_str = str(val) if val is not None else ""
            value_item = QtWidgets.QTableWidgetItem(val_str)

            self.attrib_table.setItem(i, 0, name_item)
            self.attrib_table.setItem(i, 1, type_item)
            self.attrib_table.setItem(i, 2, value_item)
            