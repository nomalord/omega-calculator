from Operator import Operator, LeftOperator, RightOperator, PairOperator, object_dict
from MathExpression import MathExpression
from Calculator import Calculator
import output as out

def clean_input(calc_string, valid_calc_string):
    """This function takes the list of numbers, parenthesis and operators and checks for validity of operator placement, and it combines minus signs that are next to each other into one minus sign or plus sign, and it combines minus signs that are next to a number or a parenthesis into a negative number or a negative parenthesis"""

    for count in range(len(calc_string)-1):
        if(type(calc_string[count]) == (int or float)):
            if(check_digit_parenth(calc_string[count+1], calc_string[count])):
                valid_calc_string.append(calc_string[count])
            else:
                print("Invalid input, there cannot be an opening parenthesis after a digit")
                print("or a closing parenthesis before a digit")
                return
        elif(isinstance(calc_string[count], Operator)):

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
                            valid_calc_string.append(object_dict['+'])
                        return clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)
                    if(count == 0 or
                       type(calc_string[toupleCheck[1]+count]) == (int or float) or
                       calc_string[count-1] == ')'):
                        if(type(calc_string[count - toupleCheck[1]]) != (int or float)):
                            valid_calc_string.append(calc_string[toupleCheck[1]+count]*-1)
                            return clean_input(calc_string[toupleCheck[1]+count+1:], valid_calc_string)  
                    valid_calc_string.append(object_dict[toupleCheck[0]])
                    return clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)

        elif(calc_string[count] == '(' or calc_string[count] == ')'):
            valid_calc_string.append(calc_string[count])
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    if(calc_string[-1] == ')' or type(calc_string[-1]) == (int or float) or isinstance(calc_string[-1], RightOperator)):
        valid_calc_string.append(calc_string[-1])

    plus_removal(valid_calc_string)
    mathh = MathExpression()
    mathh.set_expression(valid_calc_string)
    mathh.parenthesis_checker()
    calculator = Calculator(mathh.get_expression())
    mathh.result = calculator.evaluate(calculator.expression)
    out.output(mathh.result)


def check_digit_parenth(digit_check, og_operator):
    """Checks if there is a digit after a parenthesis or a parenthesis before a digit, returns false if there is"""
    if(digit_check == '('):
        return False
    return not isinstance(og_operator, LeftOperator)
    # match digit_check:
    #     case '(':
    #         return False
    #     case _:
    #         return not isinstance(og_operator, LeftOperator)


def check_operation(operation_check, og_operator):
    """Checks if there is an operation after an operation, returns false if the operations are logically correct"""
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
    """Checks if the operation is a minus, and if it is, it checks if it is logically correct"""
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
    """Checks if there are an even or odd amount of minuses in a row, returns the correct operator and the amount of minuses"""
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
    """Removes all plus signs from the string which are not operators, as they are redundant"""
    for item in range(len(valid_calc_string)-1):
        if(isinstance(valid_calc_string[item], Operator)):
            if(valid_calc_string[item].operator == '+'):
                if(isinstance(valid_calc_string[item+1], Operator)):
                    if(valid_calc_string[item+1].operator == '-'): del valid_calc_string[item]