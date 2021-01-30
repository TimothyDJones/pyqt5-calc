# h_layout.py

""" Horizontal layout example for PyQt """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QHBoxLayout")
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)
window.show()

sys.exit(app.exec_())