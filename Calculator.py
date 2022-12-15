from Operator import Operator, PairOperator, LeftOperator, RightOperator
from MathExpression import MathExpression

class Calculator:

    def __init__(self, expression):
        self.expression = expression

    def sort_expression(self, expression):
            """sorts the expression's operators by priority in a dictionary that stores index and type"""
            priority_dict = {}
            for i in range(len(expression)):
                if isinstance(expression[i], Operator):
                    if expression[i].priority not in priority_dict.keys():
                        priority_dict[expression[i].priority] = [(i, type(expression[i]))]
                    else:
                        priority_dict[expression[i].priority].append(([i], type(expression[i])))
            return priority_dict

    def evaluate(self, expression):
            """enters the mathexpression and evaluates it, if there are parenthesis it will call itself again with the expression inside the parenthesis"""
            if(len(expression) > 1):
                if(any(isinstance(iterator, MathExpression) for iterator in expression)):
                    for i in range(len(expression)):
                        if isinstance(expression[i], MathExpression):
                            self.evaluate(expression[i].get_expression())
                priority_dict = self.sort_expression(expression)
                print(priority_dict)
                if(not any(isinstance(iterator, MathExpression) for iterator in self.expression)):
                    expression = self.calculate(priority_dict, expression)
                    return expression
                
                # for i in range(len(expression)):
                #     if(isinstance(expression[i], PairOperator)):
                #         pass
                #     if(isinstance(expression[i], RightOperator)):
                #         pass
                #     if(isinstance(expression[i], LeftOperator)):
                #         pass

    def calculate(self, priority_dict, expression):
        """Calculates the expression"""
        priority_dict = dict(sorted(priority_dict.items(), reverse=True))
        for i in expression:
            if isinstance(i, Operator):
                print(i.operator, end=" ")
            else:
                print(i, end=" ")

        for key in priority_dict.keys():
            while(key in priority_dict.keys()):
                if(priority_dict[key][0][1] == PairOperator):
                        expression[priority_dict[key][0][0]].right = expression[priority_dict[key][0][0] + 1]
                        expression[priority_dict[key][0][0]].left = expression[priority_dict[key][0][0] - 1]
                        del expression[priority_dict[key][0][0] + 1]
                        del expression[priority_dict[key][0][0] - 1]
                        expression[priority_dict[key][0][0]-1] = expression[priority_dict[key][0][0]-1].operate()
                elif(priority_dict[key][0][1] == RightOperator):
                    expression[priority_dict[key][0][0]].right = expression[priority_dict[key][0][0] - 1]
                    del expression[priority_dict[key][0][0] - 1]
                    expression[priority_dict[key][0][0]-1] = expression[priority_dict[key][0][0]-1].operate()

                elif(priority_dict[key][0][1] == LeftOperator):
                    expression[priority_dict[key][0][0]].left = expression[priority_dict[key][0][0] + 1]
                    del expression[priority_dict[key][0][0] + 1]
                    expression[priority_dict[key][0][0]] = expression[priority_dict[key][0][0]].operate()

                priority_dict = self.sort_expression(expression)
                priority_dict = dict(sorted(priority_dict.items(), reverse=True))
                for i in expression:
                    if isinstance(i, Operator):
                        print(i.operator, end=" ")
                    else:
                        print(i, end=" ")
                print()
        return expression
