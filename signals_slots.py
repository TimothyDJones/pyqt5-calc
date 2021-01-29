# signals_slots.py

""" Signals and slots example for PyQt. """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Signals and Slots")
        self.layout = QVBoxLayout()
        self._createButton()
        self._createLabel()
        self.setLayout(self.layout)
        
    def _createButton(self):
        self.btn = QPushButton("Greet")
        self.btn.clicked.connect(self.greeting)
        self.layout.addWidget(self.btn)
    
    def _createLabel(self):
        self.msg = QLabel("")
        self.layout.addWidget(self.msg)
    
    def greeting(self):
        """ Slot function """
        if self.msg.text():
            self.msg.setText("")
        else:
            self.msg.setText("Hello, World!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())