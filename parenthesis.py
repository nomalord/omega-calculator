import operations as op

def parenthesis_check(string_parenthesis_check):
    countleft, countright = 0
    for char in string_parenthesis_check:
        if(char == '('):
            countleft += 1
        elif(char == ')'):
            countright += 1
    if(countleft == countright):
        return parenthesis_legal(string_parenthesis_check)
    print("Invalid input, there are an unequal amount of left and right parenthesis")
    pass
    

def parenthesis_legal(string_parenthesis_check):
    for char in string_parenthesis_check:
        match char:
            case '(':
                if(string_parenthesis_check[string_parenthesis_check.index(char)+1] == ')'):
                    print("Invalid input, there is an empty parenthesis")
                    return
                elif(string_parenthesis_check[string_parenthesis_check.index(char)+1] in op.OPERATIONS):
                    print("Invalid input, there is an operation next to a parenthesis")
                    return
            case ')':
                if(string_parenthesis_check[string_parenthesis_check.index(char)-1] == '('):
                    print("Invalid input, there is an empty parenthesis")
                    return
                elif(string_parenthesis_check[string_parenthesis_check.index(char)-1] in op.OPERATIONS):
                    print("Invalid input, there is an operation next to a parenthesis")
                    return
    pass

