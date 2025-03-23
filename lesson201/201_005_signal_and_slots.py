# Basic example of Signals and Slots (Events and Documentation)
# Signals: Events emitted by widgets (e.g., clicked, toggled, hovered).
# Slots: Functions/methods executed in response to signals.
# Decorator @Slot(): Helps Qt optimize calls between C++ (Qt) and Python.

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow,
    QPushButton, QWidget
)

# Application initialization
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('My Beautiful Window')

# Creating buttons
button1 = QPushButton('Button Text')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

# Layout setup
layout = QGridLayout()
central_widget.setLayout(layout)

# Adding buttons to the layout
layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# Slot definition: A slot is a function connected to a signal (event)

# Example Slot: Updates status bar message when called
@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('My slot has been executed')
    return inner

# Another Slot: Prints checkbox state
@Slot()
def another_slot(checked):
    print('Is it checked?', checked)

# Third Slot: Calls another_slot internally, prints checkbox state upon hover/click
@Slot()
def third_slot(action):
    def inner():
        another_slot(action.isChecked())
    return inner

# Setting up status bar
status_bar = window.statusBar()
status_bar.showMessage('Displaying message in the status bar')

# Setting up menu bar
menu = window.menuBar()
first_menu = menu.addMenu('First menu')

# First action: Updates status bar when triggered
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(slot_example(status_bar))  # type: ignore

# Second action: Checkbox-like action, prints state when toggled
second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot)  # type: ignore
second_action.hovered.connect(third_slot(second_action))  # type: ignore

# Connecting button click to third_slot (to check checkbox state)
button1.clicked.connect(third_slot(second_action))  # type: ignore

# Show window and start event loop
window.show()
app.exec()
