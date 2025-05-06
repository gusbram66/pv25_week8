import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QVBoxLayout, QHBoxLayout, QLabel
)


class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Button dan input: Choose from list
        self.list_button = QPushButton("Choose from list")
        self.list_button.clicked.connect(self.choose_from_list)
        self.list_line_edit = QLineEdit()
        layout.addLayout(self.create_row(self.list_button, self.list_line_edit))

        # Button dan input: get name
        self.name_button = QPushButton("get name")
        self.name_button.clicked.connect(self.get_name)
        self.name_line_edit = QLineEdit()
        layout.addLayout(self.create_row(self.name_button, self.name_line_edit))

        # Button dan input: Enter an integer
        self.int_button = QPushButton("Enter an integer")
        self.int_button.clicked.connect(self.get_integer)
        self.int_line_edit = QLineEdit()
        layout.addLayout(self.create_row(self.int_button, self.int_line_edit))

        self.setLayout(layout)

    def create_row(self, button, line_edit):
        h_layout = QHBoxLayout()
        h_layout.addWidget(button)
        h_layout.addWidget(line_edit)
        return h_layout

    def choose_from_list(self):
        items = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages", items, 0, False)
        if ok and item:
            self.list_line_edit.setText(item)

    def get_name(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.name_line_edit.setText(text)

    def get_integer(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number", 0, -100, 100, 1)
        if ok:
            self.int_line_edit.setText(str(num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
