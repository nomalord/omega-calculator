import operations as op
from MathExpression import MathExpression

def clean_input(calc_string, valid_calc_string):
    """Removes spaces and tabs from the input string and check"""

    calc_string = calc_string.replace(" ", "")
    calc_string = calc_string.replace("\t", "")
    for count in range(len(calc_string)):
        if(calc_string[count].isdigit()):
            if(check_digit_parenth(calc_string[count+1:])):
                valid_calc_string.append(calc_string[count])
            else:
                print("Invalid input, there cannot be an opening parenthesis after a digit")
                print("or a closing parenthesis before a digit")
                return
        elif(calc_string[count] in op.operation_object.keys() or calc_string[count] == '(' or calc_string[count] == ')'):
            if(check_operation(calc_string[count+1:], calc_string[count])):
                print("Invalid input, there cannot be two operations next to each other")
                return
            else:
                if(calc_string[count] == '-'):
                    toupleCheck = minus_clean(calc_string[count:])
                    valid_calc_string.append(toupleCheck[0])
                    clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)
                    return
                else:
                    valid_calc_string.append(calc_string[count])
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    print(valid_calc_string)
    mathh = MathExpression()
    mathh.set_expression_from_string(listToString(valid_calc_string))
    print(mathh.get_expression())
    print()

def check_digit_parenth(string_digit_check):
    """Checks if there is a parenthesis after a digit, returns false if there is"""
    for char in string_digit_check:
        match char:
            case '(':
                return False
            case _:
                return True
    return True


def check_operation(string_operation_check, og_char):
    """Checks if there are two operations back to back, returns false if they are not or if operator is -"""
    for char in string_operation_check:
        if(char in op.operation_object.keys()):
            match char:
                case '-':
                    if(og_char == '-'):
                        return False
                case '(':
                    if(og_char == '('):
                        return False
                case ')':
                    if(og_char == ')'):
                        return False
                case _:
                    if(og_char == ')'):
                        return False
                    return True
        else:
            return False
    pass

def minus_clean(string_minus_check):
    """checks if there are multiple minuses in a row, and combines them into one"""
    count = 0
    for char in string_minus_check:
        if(char == '-'):
            count += 1
        else:
            break
    if(count % 2 == 0):
        return '+', count
    else:
        return '-', count

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1



# def parenthesis_check(string_parenthesis_check):
#     count = 0
#     if(string_parenthesis_check == ""):
#         return True
#     for char_parenthesis in string_parenthesis_check:
#         match char_parenthesis:
#             case ' ':
#                 pass
#             case '\t':
#                 pass
#             case '(':
#                 return parenthesis_check(string_parenthesis_check[count+1:])
#             case ')':
#                 return False
#         count += 1

#main function
if __name__ == "__main__":
    string_calc = input("Please enter a calculation: ")
    clean_input(string_calc, [])