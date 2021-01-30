# f_layout.py

""" Dialog-style example application for PyQt """

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QLineEdit
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout

class Dialog(QDialog):
    """ Dialog """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QDialog")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())