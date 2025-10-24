import sys
from PyQt6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__(parent=None)
        self.setWindowTitle('usd_assembler')
        self.setMinimumSize(500, 200)

        self.create_widgets()
        self.create_layout()
        self.create_connections()



    def create_widgets(self):
        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)
        self.file_path_le = QtWidgets.QLineEdit()
        self.file_path_btn = QtWidgets.QPushButton('...')

        self.open_file_btn = QtWidgets.QPushButton('Open')
    def create_layout(self):
        file_layout = QtWidgets.QHBoxLayout()
        file_layout.addWidget(self.file_path_le)
        file_layout.addStretch()
        file_layout.addWidget(self.file_path_btn)


        main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        main_layout.addLayout(file_layout)
        main_layout.addWidget(self.open_file_btn)

    def create_connections(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('windows'))

    window = MainWindow()
    window.show()
    app.exec()