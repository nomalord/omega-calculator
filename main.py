operator_dict = {'+':1, '-':1, '*':2, '/':2, '^':3, '%':4, '$':5, '&':5,'@':5,'~':6,'!':6, '(':7, ')':7}


def maximum(num1, num2):
    """Returns the maximum of two numbers ($)."""
    if(num1 > num2):
        return num1
    else:
        return num2

def minimum(num1, num2):
    """Returns the minimum of two numbers (&)."""
    if(num1 < num2):
        return num1
    else:
        return num2

def average(num1, num2):
    """Returns the average of two numbers (@)."""
    return (num1 + num2) / 2

def factorial(num):
    if(num == 0):
        return 1
    else:
        return num * factorial(num - 1)

def absolute(num):
    """Returns the negative value of a number (~)."""
    num*-1