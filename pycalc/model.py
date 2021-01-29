# model.py

from pycalc.constants import *

# Simple "model" to handle calculator functionality
# This function just uses the Python "eval()" function
# to evaluate the expression entered.
def evaluateExpression(expression):
    """
    Evaluate expression in calculator display
    and return result.
    """
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
        
    return result