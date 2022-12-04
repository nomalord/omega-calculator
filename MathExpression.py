import operations as op

class MathExpression:
    def __init__(self):
        self.expression = []
        self.result = None # type: float
        self.error = None # type: str


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



    def set_expression(self, str):
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
            self.set_expression(str[count+1:])

            


#main
calc = MathExpression()
calc.set_expression("231+--23*2+~3+5#")
print(calc.expression)

