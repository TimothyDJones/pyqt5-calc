# view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

# Main view class for calculator GUI
class PyCalcUi(QMainWindow):
    """
    Main calculator GUI
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        
        # Define general layout main widget for the calculator GUI
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # Create the calculator display and buttons
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        """
        Calculator display/output
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        """
        Calculator buttons
        """
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text: position on QGridLayout
        buttons = {"7": (0, 0),
                   "8": (0, 1),
                   "9": (0, 2),
                   "/": (0, 3),
                   "C": (0, 4),
                   "4": (1, 0),
                   "5": (1, 1),
                   "6": (1, 2),
                   "*": (1, 3),
                   "(": (1, 4),
                   "1": (2, 0),
                   "2": (2, 1),
                   "3": (2, 2),
                   "-": (2, 3),
                   ")": (2, 4),
                   "0": (3, 0),
                   "00": (3, 1),
                   ".": (3, 2),
                   "+": (3, 3),
                   "=": (3, 4),
                  }
        # Create buttons and add to grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        """
        Set the text/content in calculator display
        """
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        """
        Get current text/content from calculator display
        """
        return self.display.text()
        
    def clearDisplay(self):
        """
        Clear calculator display
        """
        self.setDisplayText("")