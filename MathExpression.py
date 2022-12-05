import operations as op

class MathExpression:
    def __init__(self):
        self.expression = []
        self.result = None # type: float
        self.error = None # type: str

    def __str__(self) -> str:
        return "math"

    # def minus_clean(self):
    #     for i in range(len(self.expression)):
    #         if(self.expression[i] == '-'):
    #             if(i != 0):
    #                 if(self.expression[i-1].isdigit()):
    #                     continue
    #     pass

    # def evaluate(self):
    #     try:
    #         for i in range(len(self.expression)):
    #             pass
    #         pass
    #     except:
    #         self.error = "Error"
    #         pass



    def set_expression_from_string(self, str):
        count = 0
        if(str[count].isdigit()):
            str_num = str[count]
            while(str[count+1].isdigit()):
                    count += 1
                    str_num += str[count]
                    if(count+1 == len(str)):
                        break
            self.expression.append(int(str_num))
        else:
            self.expression.append(str[count])
        if(count+1 < len(str)):
            self.set_expression_from_string(str[count+1:])

    def set_expression(self, expression):
        self.expression = expression


    def parenthesis_checker(self):
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


count = MathExpression()
count.set_expression_from_string("(9+22-(3+5))(3+(5)-6)")
count.parenthesis_checker()
count.parenthesis_list_index()
print(count.expression)


# list = [5,8,7,6,5,4]
# del list[2:6]
# print(list)