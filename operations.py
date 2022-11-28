operator_dict = {'+':1, '-':1, '*':2, '/':2, '^':3, '%':4,
                 '$':5, '&':5, '@':5, '~':6, '!':6}

OPERATIONS = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '(', ')']

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def modulus(num1, num2):
    return num1 % num2

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
    """Returns the factorial of a number (!)."""
    if(num == 0):
        return 1
    else:
        return num * factorial(num - 1)

def negative(num):
    """Returns the negative value of a number (~)."""
    num*-1