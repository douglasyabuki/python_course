# QMainWindow and centralWidget structure
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (button1)
#               -> Widget 2 (button2)
#               -> Widget 3 (button3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow,
    QPushButton, QWidget
)

# Initialize the application
app = QApplication(sys.argv)

# Main window creation
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('My Beautiful Window')

# Button 1
button1 = QPushButton('Button Text')
button1.setStyleSheet('font-size: 80px;')

# Button 2
button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

# Button 3
button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

# Creating a grid layout
layout = QGridLayout()
central_widget.setLayout(layout)

# Positioning buttons in the grid layout
layout.addWidget(button1, 1, 1, 1, 1)      # row 1, column 1
layout.addWidget(button2, 1, 2, 1, 1)      # row 1, column 2
layout.addWidget(button3, 3, 1, 1, 2)      # row 3, column 1 spanning 2 columns

# Example slot (function connected to signal)
def slot_example(status_bar):
    status_bar.showMessage('My slot has been executed')

# Status bar setup
status_bar = window.statusBar()
status_bar.showMessage('Display message in the status bar')

# Menu bar setup
menu = window.menuBar()
first_menu = menu.addMenu('First Menu')
first_action = first_menu.addAction('First Action')

# Connecting the action signal to slot_example
first_action.triggered.connect(  # type: ignore
    lambda: slot_example(status_bar)
)

# Show window
window.show()

# Run the application loop
app.exec()
