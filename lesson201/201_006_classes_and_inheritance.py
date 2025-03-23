# Working with classes and inheritance using PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow,
    QPushButton, QWidget
)

# Class inheriting from QMainWindow to create a custom window
class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Creating the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('My Beautiful Window')

        # Buttons creation
        self.button1 = self.make_button('Button Text')
        self.button1.clicked.connect(self.second_action_checked)  # type: ignore

        self.button2 = self.make_button('Button 2')
        self.button3 = self.make_button('Third')

        # Grid layout configuration
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Adding buttons to the grid layout
        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        # Status bar setup
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Showing a message in the status bar')

        # Menu bar setup
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('First menu')

        # First action in menu bar
        self.first_action = self.first_menu.addAction('First action')
        self.first_action.triggered.connect(self.change_status_bar_message)

        # Second action in menu bar (checkable)
        self.second_action = self.first_menu.addAction('Second action')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_checked)
        self.second_action.hovered.connect(self.second_action_checked)

    @Slot()
    def change_status_bar_message(self):
        self.status_bar.showMessage('My slot was executed')

    @Slot()
    def second_action_checked(self):
        print('Is checked?', self.second_action.isChecked())

    def make_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet('font-size: 80px;')
        return button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # Application event loop
