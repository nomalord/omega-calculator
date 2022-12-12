import operations as op

class MathExpression:
    def __init__(self):
        self.expression = []
        self.result = None # type: float
        self.error = None # type: str

    def __str__(self) -> str:
        return "math"


    def set_expression_from_string(self, input_list_str):
        """Sets the expression from a string"""
        count = 0
        if(input_list_str[count].isdigit()):
            str_num = input_list_str[count]
            if(count+1 != len(input_list_str)):
                while(input_list_str[count+1].isdigit()):
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
                    self.expression.append(op.operation_object[input_list_str[count]])
        if(count+1 < len(input_list_str)):
            self.set_expression_from_string(input_list_str[count+1:])

        self.parenthesis_checker()
        self.parenthesis_list_index()


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
        self.parenthesis_tokenizer()


    def parenthesis_tokenizer(self):
        
        pass

    def parenthesis_list_index(self):
        """Finds the index of the parenthesis and creates a new MathExpression object for the expression inside the parenthesis"""
        stack = []
        for i in range(len(self.expression)):
            if self.expression[i] == "(":
                stack.append(i)
            elif self.expression[i] == ")":
                pop = stack.pop()
                layered_expression = MathExpression()
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


    # def evaluate(self):
    #     try:
    #         for i in range(len(self.expression)):
    #             pass
    #         pass
    #     except:
    #         self.error = "Error"
    #         pass


# count = MathExpression()
# count.set_expression_from_string("(9+22-(3+5))(3+(5)-6)")
# count.parenthesis_checker()
# count.parenthesis_list_index()
# print(count.expression)


# list = [5,8,7,6,5,4]
# del list[2:6]
# print(list)