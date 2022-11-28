def parenthesis_check(string_parenthesis_check):
    countleft, countright = 0
    for char in string_parenthesis_check:
        if(char == '('):
            countleft += 1
        elif(char == ')'):
            countright += 1
    if(countleft == countright):
        return True
    pass

def parenthesis_legal(string_parenthesis_check):
    
            