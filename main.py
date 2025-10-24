import sys
from PyQt6 import QtWidgets

import usd_utils
from widgets.file_browser import FileBrowser

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
        # file_layout.addStretch()
        file_layout.addWidget(self.file_path_btn)


        main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        main_layout.addLayout(file_layout)
        main_layout.addWidget(self.open_file_btn)

    def create_connections(self):
        self.file_path_btn.clicked.connect(self.open_file_dialog)
        self.open_file_btn.clicked.connect(self.open_file)

    def open_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.file_path_le.setText(selected_files[0])
            return selected_files[0]
    
    def open_file(self):
        try:
            usd_utils.open_file(self.file_path_le.text())
            window = FileBrowser(self)
            window.exec()
        except usd_utils.WrongFileFormatError as e:
            self.error_message("not supported file format!")

    def error_message(self, message):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText(message)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        dlg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok
        )
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.StandardButton.Ok:
            print("OK!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('windows'))

    window = MainWindow()
    window.show()
    app.exec()