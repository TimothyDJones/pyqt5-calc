# hello-qt5.py

""" Simple 'Hello, World!' for PyQt """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 Application")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60,15)
window.show()

sys.exit(app.exec_())