from Operator import PairOperator, RightOperator, LeftOperator, Operator, object_dict

class MathExpression:
    def __init__(self):
        self.expression = []
        self.result = None # type: float
        self.negative = False

    def __str__(self) -> str:
        return "math"


    def set_expression_from_string(self, input_list_str):
        """This function takes a string and converts it into a list of numbers, parenthesis and operators"""
        try:
            count = 0
            if(input_list_str[count]).isdigit():
                str_num = input_list_str[count]
                if(count+1 != len(input_list_str)):
                    while (input_list_str[count+1]).isdigit() or input_list_str[count+1] == '.':
                            count += 1
                            str_num += input_list_str[count]
                            if(count+1 == len(input_list_str)):
                                break
                            if(input_list_str[count+1] == '.' and '.' in str_num):
                                raise ValueError("invalid input, two dots in a number")
                if str_num.isdigit():
                    self.expression.append(int(str_num))
                else:
                    self.expression.append(float(str_num))
            elif input_list_str[count] == '.':
                str_num = input_list_str[count]
                if(count+1 != len(input_list_str)):
                    while (input_list_str[count+1]).isdigit():
                            count += 1
                            str_num += input_list_str[count]
                            if(count+1 == len(input_list_str)):
                                break
                            if(input_list_str[count+1] == '.' and '.' in str_num):
                                raise ValueError("invalid input, two dots in a number")
                self.expression.append(float(str_num))
            else:
                if(input_list_str[count] not in object_dict.keys()):
                    self.expression.append(input_list_str[count])
                else:
                    self.expression.append(object_dict[input_list_str[count]])
                # match input_list_str[count]:
                #     case '(':
                #         self.expression.append('(')
                #     case ')':
                #         self.expression.append(')')
                #     case _:
                #         if(input_list_str[count] not in object_dict.keys()):
                #             self.expression.append(input_list_str[count])
                #         else:
                #             self.expression.append(object_dict[input_list_str[count]])
            if(count+1 < len(input_list_str)):
                self.set_expression_from_string(input_list_str[count+1:])
        except ValueError as e:
            print(e)
            from start import main
            main()
            
    def parenthesis_checker(self):
        """Checks if the parenthesis are valid"""
        try:
            countleft, countright = 0, 0
            for i in range(len(self.expression)):
                if(self.expression[i] == '(' or self.expression[i] == '{'):
                    countleft += 1
                elif(self.expression[i] == ')'):
                    if(self.expression[i-1] == '('):
                        from Exceptions import ParenthesisError
                        raise ParenthesisError("parenthesis are invalid")
                    countright += 1
            if(countleft != countright):
                from Exceptions import ParenthesisError
                raise ParenthesisError("Invalid input, there are an unequal amount of left and right parenthesis")
                
            self.parenthesis_list_index()

        except ParenthesisError as e:
            print(e)
            from start import main
            main()

    def parenthesis_list_index(self):
        """This function takes the list of numbers, parenthesis and operators and converts it into a list of numbers, parenthesis and operators, and a list of the indexes of the parenthesis"""
        stack = []
        for i in range(len(self.expression)):
            if self.expression[i] == "(":
                stack.append(i)
            elif self.expression[i] == "{":
                stack.append((i, "{"))
            elif self.expression[i] == ")":
                pop = stack.pop()
                layered_expression = MathExpression()
                if isinstance(pop, tuple):
                    layered_expression.set_expression(self.expression[pop[0]+1:i])
                    del self.expression[pop[0]+1:i+1]
                    layered_expression.negative = True
                    self.expression[pop[0]] = layered_expression
                    self.parenthesis_list_index()
                    return
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