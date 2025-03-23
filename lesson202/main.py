import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Set the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info label
    info = Info('Your calculation')
    window.addWidgetToVLayout(info)

    # Display input
    display = Display()
    window.addWidgetToVLayout(display)

    # Buttons grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vertical_layout.addLayout(buttonsGrid)

    # Run everything
    window.adjustFixedSize()
    window.show()
    app.exec()
