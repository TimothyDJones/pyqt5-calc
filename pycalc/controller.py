# controller.py

from functools import partial

from pycalc.constants import *

# Main calculator controller class
# Connects the view (GUI) with the model (business logic)
class PyCalcCtrl():
    """
    Main calculator controller class
    """
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()  # Register signals/slots
    
    def _calculateResult(self):
        """
        Evaluate expression in calculator display.
        """
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
        
    def _buildExpression(self, sub_exp):
        """
        Build expression for calculation to perform.
        """
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
            
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
        
    def _connectSignals(self):
        """
        Register associations between button clicks ("signals")
        and their actions ("slots").
        """
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        
        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)