from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Setting up the basic layout
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

        # Window title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        # Should be called as the last step
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)

    def createMessageBox(self):
        return QMessageBox(self)
