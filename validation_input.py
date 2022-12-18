import Operator as op

def first_cleaning(calc_string, valid_calc_string):
    """This function cleans the input of the user, it removes all spaces and tabs, and checks if the input is valid, if it is, it will be sent to the clean_input function in the clean_equation.py file, if the input is invalid, the user will be asked to enter a valid input."""

    calc_string = calc_string.replace(" ", "")
    calc_string = calc_string.replace("\t", "")
    for count in range(len(calc_string)):
        if(calc_string[count].isdigit()):
            valid_calc_string.append(calc_string[count])
        elif(calc_string[count] in op.object_dict.keys() or calc_string[count] == '(' or calc_string[count] == ')'):
            valid_calc_string.append(calc_string[count])
            
        else:
            from Exceptions import InputError
            raise InputError("invalid input, only parenthesis, numbers and operations are allowed")

    # math_expression = MathExpression()
    # math_expression.set_expression_from_string(valid_calc_string)
    return valid_calc_string