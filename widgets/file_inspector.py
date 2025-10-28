import sys
from PyQt6 import QtWidgets, QtCore
from widgets.attributes import Attributes
import usd_utils
from pxr import Sdf, UsdShade


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
        # PRIM TREE
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setHeaderLabels(['Name', 'Type'])
        for p in self.stage.Traverse():
            self.populate_tree(p, self.tree_widget)
        self.tree_widget.resizeColumnToContents(0)
        self.tree_widget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        # LAYERS TREE
        self.layer_tree_widget = QtWidgets.QTreeWidget()
        self.layer_tree_widget.setColumnCount(2)
        self.layer_tree_widget.setHeaderLabels(["Layer", "Type"])
        self.populate_layers_tree(self.stage.GetRootLayer())

        # TABS
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.addTab(self.tree_widget, "prims")
        self.tab_widget.addTab(self.layer_tree_widget, "layers")
        self.tab_widget.addTab(QtWidgets.QLabel('materials'), 'materials')
        
        self.seprate_button = QtWidgets.QPushButton('export')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.seprate_button)
    def create_connections(self):
        self.tree_widget.itemDoubleClicked.connect(self.on_cell_clicked)
        self.seprate_button.clicked.connect(self.on_export_clicked)


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

    def on_export_clicked(self):
        sel_items = self.tree_widget.selectedItems()

        new_stage = usd_utils.create_new_file("assembeled.usda")
        for i, item in enumerate(sel_items):
            name = item.text(0)
            type_ = item.text(1)
            prim_path = item.data(0, QtCore.Qt.ItemDataRole.UserRole)
            print(f"{name} ({type_}) -> {prim_path}")
            
            # usd_utils.copy_prim(self.stage, prim_path, new_stage)
            usd_utils.refrence_to_destination(self.stage, prim_path, new_stage)



    def populate_layers_tree(self, layer, parent_item=None):
        item = QtWidgets.QTreeWidgetItem([
                    layer.identifier,
                    "root" if parent_item is None else "sublayer"
        ])

        item.setData(0, QtCore.Qt.ItemDataRole.UserRole, layer)

        if parent_item:
            parent_item.addChild(item)
        else:
            self.layer_tree_widget.addTopLevelItem(item)

        for sublayer_path in layer.subLayerPaths:
            sublayer = Sdf.Layer.FindRelativeToLayer(layer, sublayer_path)
            if sublayer:
                self.layer_tree_widget.populate(sublayer, item)


    def get_materials(self):
        materials = []
        for prim in self.stage.Traverse():
            if prim.IsA(UsdShade.Material):
                materials.append(UsdShade.Material(prim))

        print("Found materials:")
        for mat in materials:
            print("-", mat.GetPath())