import operations as op
from Operator import PairOperator, RightOperator, LeftOperator, Operator

class MathExpression:
    def __init__(self):
        self.expression = []
        self.result = None # type: float
        self.parenth_exist = False # type: bool

    def __str__(self) -> str:
        return "math"


    def set_expression_from_string(self, input_list_str):
        """Sets the expression from a string"""
        count = 0
        if(input_list_str[count]).isdigit():
            str_num = input_list_str[count]
            if(count+1 != len(input_list_str)):
                while(input_list_str[count+1]).isdigit():
                        count += 1
                        str_num += input_list_str[count]
                        if(count+1 == len(input_list_str)):
                            break
            self.expression.append(int(str_num))
        else:
            match input_list_str[count]:
                case '(':
                    self.expression.append('(')
                case ')':
                    self.expression.append(')')
                case _:
                    if(input_list_str[count] not in op.operation_object.keys()):
                        self.expression.append(input_list_str[count])
                    else:
                        self.expression.append(op.operation_object[input_list_str[count]])
        if(count+1 < len(input_list_str)):
            self.set_expression_from_string(input_list_str[count+1:])

    def parenthesis_checker(self):
        """Checks if there are an equal amount of left and right parenthesis"""
        countleft, countright = 0, 0
        for i in range(len(self.expression)):
            if(self.expression[i] == '('):
                countleft += 1
            elif(self.expression[i] == ')'):
                if(self.expression[i-1] == '('):
                    print("parenthesis are invalid")
                    return
                countright += 1
        if(countleft != countright):
            print("Invalid input, there are an unequal amount of left and right parenthesis")
            return
        self.parenthesis_list_index()

    def parenthesis_list_index(self):
        """Finds the index of the parenthesis and creates a new MathExpression object for the expression inside the parenthesis"""
        stack = []
        for i in range(len(self.expression)):
            if self.expression[i] == "(":
                stack.append(i)
            elif self.expression[i] == ")":
                pop = stack.pop()
                layered_expression = MathExpression()
                self.parenth_exist = True
                layered_expression.set_expression(self.expression[pop+1:i])
                del self.expression[pop+1:i+1]
                self.expression[pop] = layered_expression
                self.parenthesis_list_index()
                return
    pass
    def get_expression(self):
        return self.expression

    def set_expression(self, expression):
        self.expression = expression

    # def left_right_operator_check(self):
    #     """checks if left/right operators in expression are valid"""
    #     for i in range(len(self.expression)):
    #         if isinstance(self.expression[i], op.RightOperator):
    #             if i+1 < len(self.expression):
    #                 if(self.expression[i+1] == '(' or type(self.expression[i+1]) == int):
    #                     print("Invalid input, there cannot be a number after the operator")
    #                     return False
    #         elif isinstance(self.expression[i], op.LeftOperator):
    #             if i != 0:
    #                 if(self.expression[i-1] == ')' or type(self.expression[i-1]) == int):
    #                     print("Invalid input, there cannot be a number before the operator")
    #                     return False
    #                 if(isinstance(self.expression[i-1], op.PairOperator)):
    #                     if(i-2 < 0 or self.expression[i-2] == '('):
    #                         self.expression[i-1] = '-'
    #                         continue
    #                     else:
    #                         print("Invalid input, there cannot be a minus before a left operator")
    #                         return False
    
    #     return True

    def sort_expression(self):
        """sorts the expression's operators by priority in a dictionary that stores index"""
        priority_dict = {}
        for i in range(len(self.expression)):
            if isinstance(self.expression[i], Operator):
                if self.expression[i].priority not in priority_dict.keys():
                    priority_dict[self.expression[i].priority] = [i]
                else:
                    priority_dict[self.expression[i].priority].append(i)
        return priority_dict
    
    def evaluate(self):
        if(self.parenth_exist):
            for i in range(len(self.expression)):
                if isinstance(self.expression[i], MathExpression):
                    self.expression[i].evaluate()
        else:
            for i in range(len(self.expression)):
                if(isinstance(self.expression[i], op.PairOperator)):
                    pass
                if(isinstance(self.expression[i], op.RightOperator)):
                    pass
                if(isinstance(self.expression[i], op.LeftOperator)):
                    pass


# count = MathExpression()
# count.set_expression_from_string("(9+22-(3+5))(3+(5)-6)")
# count.parenthesis_checker()
# count.parenthesis_list_index()
# print(count.expression)


# list = [5,8,7,6,5,4]
# del list[2:6]
# print(list)