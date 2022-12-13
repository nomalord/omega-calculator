import operator as op

class Operator():
    def __init__(self, operator, priority):
        self.operator = operator
        self.priority = priority

    def __str__(self):
        return self.operator

    def action():
        pass

class PairOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.left = None
        self.right = None

    def action(self):
        match self.operator:
            case "+":
                return op.add(self.left, self.right)
            case "-":
                return op.subtract(self.left, self.right)
            case "*":
                return op.multiply(self.left, self.right)
            case "/":
                return op.divide(self.left, self.right)
            case "^":
                return op.power(self.left, self.right)
            case "%":
                return op.modulus(self.left, self.right)
            case "$":
                return op.maximum(self.left, self.right)
            case "&":
                return op.minimum(self.left, self.right)
            case "@":
                return op.average(self.left, self.right)
            case _: # default
                return None

class RightOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.right = None

    def action(self):
        match self.operator:
            case "!":
                return op.factorial(self.right)
            case "#":
                return op.sum_digits(self.right)
            case _: # default
                return None

class LeftOperator(Operator):
    def __init__(self, operator, priority):
        super().__init__(operator, priority)
        self.left = None

    def action(self):
        match self.operator:
            case "~":
                return op.negative(self.left)
            case _: # default
                return None