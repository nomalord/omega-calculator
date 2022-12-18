class Operator():
    def __init__(self, operator, priority):
        self.operator = operator
        self.priority = priority

    def __str__(self):
        return self.operator

    def operate():
        pass

class PairOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.left = None
        self.right = None

    def operate(self):
        return function_dict[self.operator](self.left, self.right)

class RightOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.right = None

    def operate(self):
        return function_dict[self.operator](self.right)

class LeftOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.left = None

    def operate(self):
        return function_dict[self.operator](self.left)


object_dict = {'+':PairOperator('+', 1),'-': PairOperator('-', 1),'*': PairOperator('*', 2),
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
        raise ZeroDivisionError("Cannot divide by zero.")

def power(num1, num2):
    if(num1 == 0 and num2 < 0):
        raise ZeroDivisionError("Cannot divide by zero.")
    elif(num1 < 0 and num2 % 1 != 0):
        raise ValueError("Cannot raise a negative number to a non-integer power.")
    elif(num1**num2 == float('inf')):
        raise OverflowError("Cannot raise a number to a power that large.")
    elif(num1**num2 is complex):
        raise ValueError("complex solutions are not accepted.")
    return num1 ** num2

def power_wrapper(num1, num2, test_check = False):
    try:
        return power(num1, num2)
    except OverflowError as e:
        print(e)
        from start import main
        main(test = test_check)
    except ValueError as e:
        print(e)
        from start import main
        main(test = test_check)
    except ZeroDivisionError as e:
        print(e)
        from start import main
        main(test = test_check)

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
    if(num < 0):
        raise ValueError("Cannot take the factorial of a negative number.")
    if(type(num) == float):
        float_str = str(num)
        if(float_str.split('.')[1] != '0' and len(float_str[1]) > 1):
            raise TypeError("Cannot take the factorial of a non-integer.")
    if(num == 0):
            return 1
    else:
        return num * factorial(num - 1)

def factorial_wrapper(num, test_check = False):
    try:
        return factorial(num)
    except RecursionError as e:
        print(e)
        from start import main
        main(test = test_check)
    except TypeError as e:
        print(e)
        from start import main
        main(test = test_check)
    except ValueError as e:
        print(e)
        from start import main
        main(test = test_check)


def negative(num):
    """Returns the negative value of a number (~)."""
    return num*-1

def sum_digits(num):
    """returns the sum of a the digits of a number (#)."""
    flag = False
    if(num < 0):
        num *= -1
        flag = True
    sum = 0
    while(num >= 1):
        sum += num % 10
        num = num // 10
    if(flag):
        sum *= -1
    return sum


function_dict = {'+':add,'-':subtract,'*':multiply,'/':divide,'^':power_wrapper,'%':modulus,'$':maximum,
                 '&':minimum,'@':average,'~':negative,'!':factorial_wrapper,'#':sum_digits}