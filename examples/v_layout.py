# v_layout.py

""" Vertical layout example for PyQt """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QVBoxLayout")
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)
window.show()

sys.exit(app.exec_())