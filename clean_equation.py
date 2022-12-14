from Operator import Operator, LeftOperator, RightOperator, PairOperator
from operations import operation_object
from MathExpression import MathExpression

def clean_input(calc_string, valid_calc_string):
    """check for invalid input with logic of operaions and parenthesis"""

    for count in range(len(calc_string)-1):
        if(type(calc_string[count]) == (int or float)):
            if(check_digit_parenth(calc_string[count+1], calc_string[count])):
                valid_calc_string.append(calc_string[count])
            else:
                print("Invalid input, there cannot be an opening parenthesis after a digit")
                print("or a closing parenthesis before a digit")
                return
        elif(isinstance(calc_string[count], Operator)):

            # num_check_before_minus = (calc_string[count].operator == '-' and 
            # (count == 0 or calc_string[count-1].isdigit() or 
            # calc_string[count-1] == ')' or 
            # calc_string[count-1] == '('))

            if(check_operation(calc_string[count+1], calc_string[count])):
                print("Invalid input, there cannot be two operations next to each other that are"+
                "not minuses or an operation next to a minus without a number or bracket before it")
                return
                
            else:
                if(calc_string[count].operator != '-'): 
                    valid_calc_string.append(calc_string[count])
                else:
                    toupleCheck = minus_clean(calc_string[count:])
                    if(toupleCheck[0] == '+'):
                        if(type((calc_string[toupleCheck[1]+count]) == (int or float) or
                           isinstance(calc_string[toupleCheck[1]+count],LeftOperator)) and
                           count != 0 and
                           calc_string[count-1] != '(' and
                           calc_string[count-1] != '+'): 
                            valid_calc_string.append(operation_object['+'])
                        return clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)
                    if(count == 0 or
                       type(calc_string[toupleCheck[1]+count]) == (int or float) or
                       calc_string[count-1] == ')'):
                        if(type(calc_string[count - toupleCheck[1]]) != (int or float)):
                            valid_calc_string.append(calc_string[toupleCheck[1]+count]*-1)
                            return clean_input(calc_string[toupleCheck[1]+count+1:], valid_calc_string)  
                    valid_calc_string.append(toupleCheck[0])
                    return clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)

        elif(calc_string[count] == '(' or calc_string[count] == ')'):
            valid_calc_string.append(calc_string[count])
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    if(calc_string[-1] == ')'):
        valid_calc_string.append(calc_string[-1])

    plus_removal(valid_calc_string)
    mathh = MathExpression()
    mathh.set_expression(valid_calc_string)
    # if(not mathh.left_right_operator_check()):
    #     return
    mathh.parenthesis_checker()
    mathh.sort_expression()
    print(mathh.get_expression())


def check_digit_parenth(digit_check, og_operator):
    """Checks if there is a parenthesis after a digit, returns false if there is"""
    match digit_check:
        case '(':
            return False
        case _:
            return not isinstance(og_operator, LeftOperator)


def check_operation(operation_check, og_operator):
    """Checks if there are two operations back to back, unless they are not pair operations, returns false if they are not or if operator is -"""
    if(isinstance(operation_check, Operator)):
        check_operator_type(operation_check, og_operator)

    elif(type(operation_check) == (int or float) and not
    isinstance(og_operator, RightOperator)):
        return False
    else:
        if(operation_check == ')'):
            if(isinstance(og_operator, LeftOperator)):
                return True
        else:
            if(isinstance(og_operator, RightOperator)):
                return True
        return False
    pass

def check_operator_type(operation_check, og_operator):
    if(isinstance(operation_check, PairOperator)):
        if(operation_check.operator == '-'):
            if(isinstance(og_operator, RightOperator)):
                return True
            return False
        if(isinstance(og_operator, PairOperator)):
            return True
        return False

    elif(isinstance(operation_check, RightOperator)):
        if(og_operator != ')' or not
            type(og_operator) == (int or float) or not
            isinstance(og_operator, RightOperator)):
            return True
        return False

    elif(isinstance(operation_check, LeftOperator)):
        if(og_operator != '(' or not
            type(og_operator) == (int or float) or not
            isinstance(og_operator, LeftOperator)):
            return True
        return False

def minus_clean(string_minus_check):
    """checks if there are multiple minuses in a row, and combines them into one"""
    count = 0
    for obj in string_minus_check:
        if(isinstance(obj, Operator)):
            if(obj.operator == '-'):
                count += 1
            else:
                break
        else:
            break
    if(count % 2 == 0):
        return '+', count
    else:
        return '-', count

def plus_removal(valid_calc_string):
    for item in range(len(valid_calc_string)-1):
        if(isinstance(valid_calc_string[item], Operator)):
            if(valid_calc_string[item].operator == '+'):
                if(isinstance(valid_calc_string[item+1], Operator)):
                    if(valid_calc_string[item+1].operator == '-'): del valid_calc_string[item]




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