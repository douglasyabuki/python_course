# QWidget and QLayout from PySide6.QtWidgets
# QWidget -> A generic widget
# QLayout -> A layout widget that arranges other widgets
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)  # Main application object

# Create first button
button = QPushButton('Button Text')
button.setStyleSheet('font-size: 80px;')

# Create second button
button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

# Create third button
button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

# Create a central widget
central_widget = QWidget()

# Create a grid layout and set it as the layout of the central widget
layout = QGridLayout()
central_widget.setLayout(layout)

# Add buttons to specific positions in the grid layout
layout.addWidget(button, 1, 1, 1, 1)      # row 1, column 1
layout.addWidget(button2, 1, 2, 1, 1)     # row 1, column 2
layout.addWidget(button3, 3, 1, 1, 2)     # row 3, column 1, spanning 2 columns

central_widget.show()  # Display the central widget window

app.exec()  # Run the application event loop
