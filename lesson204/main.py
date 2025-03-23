import sys
import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = '0'
        self.started.emit(value)
        for i in range(50, 100, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.3)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)  # type: ignore
        self.button2.clicked.connect(self.hardWork2)  # type: ignore

    def hardWork1(self):
        self._worker1 = Worker1()
        self._thread1 = QThread()

        # Ensure the widget keeps a reference to the worker and the thread
        worker = self._worker1
        thread = self._thread1

        # Move the worker to the thread. All functions and methods of
        # the worker object will now run inside the QThread's context.
        worker.moveToThread(thread)

        # When a QThread starts, it automatically emits the "started" signal.
        thread.started.connect(worker.doWork)  # type: ignore

        # The worker emits "finished" when its task is done.
        # This triggers the thread's "quit" method to stop its event loop.
        worker.finished.connect(thread.quit)

        # deleteLater schedules the worker object for deletion from Python's
        # memory management system once the worker finishes and emits "finished".
        thread.finished.connect(thread.deleteLater)  # type: ignore
        worker.finished.connect(worker.deleteLater)

        # Connect your custom slots to handle start, progress, and finish
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        # Start the thread
        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker 1 started', value)

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('1 in progress', value)

    def worker1Finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)
        print('worker 1 finished', value)

    def hardWork2(self):
        self._worker2 = Worker2()
        self._thread2 = QThread()

        # Ensure the widget keeps a reference to the worker and the thread
        worker = self._worker2
        thread = self._thread2

        # Move the worker to the thread
        worker.moveToThread(thread)

        # QThread emits "started" automatically when started
        # Method name is "executeMe" for this example
        thread.started.connect(worker.executeMe)  # type: ignore

        # Same cleanup logic as worker1
        worker.finished.connect(thread.quit)
        thread.finished.connect(thread.deleteLater)  # type: ignore
        worker.finished.connect(worker.deleteLater)

        # Custom slots
        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        # Start the thread
        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 started', value)

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('2 in progress', value)

    def worker2Finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)
        print('worker 2 finished', value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
