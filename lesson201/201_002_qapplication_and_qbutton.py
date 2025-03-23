# QApplication and QPushButton from PySide6.QtWidgets
# QApplication -> The main widget (application) object
# QPushButton -> A clickable button
# PySide6.QtWidgets -> Contains all widgets provided by PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)  # Main application widget, handling system args

button = QPushButton('Button Text')  # Create a button widget with text
button.setStyleSheet('font-size: 40px;')  # Set CSS style for button
button.show()  # Adds the widget to the hierarchy and displays the window

app.exec()  # Runs the application's event loop
