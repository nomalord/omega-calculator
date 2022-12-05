import operations as op
import MathExpression as mp



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
    

# def parenthesis_legal(string_parenthesis_check):
#     for char in string_parenthesis_check:
#         match char:
#             case '(':
#                 if(string_parenthesis_check[string_parenthesis_check.index(char)+1] == ')'):
#                     print("Invalid input, there is an empty parenthesis")
#                     return
#                 elif(string_parenthesis_check[string_parenthesis_check.index(char)+1] in op.OPERATIONS):
#                     print("Invalid input, there is an operation next to a parenthesis")
#                     return
#             case ')':
#                 if(string_parenthesis_check[string_parenthesis_check.index(char)-1] == '('):
#                     print("Invalid input, there is an empty parenthesis")
#                     return
#                 elif(string_parenthesis_check[string_parenthesis_check.index(char)-1] in op.OPERATIONS):
#                     print("Invalid input, there is an operation next to a parenthesis")
#                     return
#     pass


# def parenthesis_tokenizer(str_expression):
#     touple_list_parenthe_index = []
#     for i in range(len(str_expression)):
#         if(str_expression[i] == '('):
#             touple_list_parenthe_index.append(('(', i))
#         elif(str_expression[i] == ')'):
#             touple_list_parenthe_index.append((')', i))
#     parenthesis_Math_Expression_combined(touple_list_parenthe_index, str_expression)

# def parenthesis_Math_Expression_combined(touple_list_parenthe_index, str_expression):
#     math_expression = mp.MathExpression()
#     for i in range(len(touple_list_parenthe_index)):
#         if(touple_list_parenthe_index[i][0] == '('):
#             if(touple_list_parenthe_index[i+1][0] == ')'):
#                 math_expression.expression.append(mp.MathExpression(str_expression[touple_list_parenthe_index[i][1]+1:touple_list_parenthe_index[i+1][1]]))
#                 str_expression.
#                 str_expression.split().remove(str_expression[touple_list_parenthe_index[i][1]+1:touple_list_parenthe_index[i+1][1]])
#                 touple_list_parenthe_index.remove(touple_list_parenthe_index[i])
#                 touple_list_parenthe_index.remove(touple_list_parenthe_index[i+1])
                
            

#     return touple_list_parenthe_index

#print(parenthesis_tokenizer("2+3*(4+5)"))

touple = (1, 2)

list = [5,8,7,2]
print(list)
list.remove(8)
print(list)
st = "lololol"

