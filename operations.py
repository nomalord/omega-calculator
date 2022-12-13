from Operator import PairOperator, RightOperator, LeftOperator

operation_object = {'+':PairOperator('+', 1),'-': PairOperator('-', 1),'*': PairOperator('*', 2),
                    '/':PairOperator('/', 2),'^': PairOperator('^', 3),'%': PairOperator('%', 4),
                    '$':PairOperator('$', 5),'&': PairOperator('&', 5),'@': PairOperator('@', 5),
                    '~':LeftOperator('~', 6),'!': RightOperator('!', 6),'#': RightOperator('#', 6)}

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try :
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero.")
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
    try:
        if(num == 0):
            return 1
        else:
            return num * factorial(num - 1)
    except RecursionError:
        print("Cannot take the factorial of a number that large.")
    

def negative(num):
    """Returns the negative value of a number (~)."""
    num*-1

def sum_digits(num):
    """returns the sum of a the digits of a number (#)."""
    sum = 0
    while(num > 0):
        sum += num % 10
        num = num // 10
    return sum