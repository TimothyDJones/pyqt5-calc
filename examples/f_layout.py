# f_layout.py

""" Form layout example for PyQt """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QFormLayout")
layout = QFormLayout()
layout.addRow("Name:", QLineEdit())
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)
window.show()

sys.exit(app.exec_())