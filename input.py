from clean_equation import clean_input
from MathExpression import MathExpression
import Operator as op

def first_cleaning(calc_string, valid_calc_string):
    """Removes spaces and tabs from the input string and checks for invalid characters"""

    calc_string = calc_string.replace(" ", "")
    calc_string = calc_string.replace("\t", "")
    for count in range(len(calc_string)):
        if(calc_string[count].isdigit()):
            valid_calc_string.append(calc_string[count])
        elif(calc_string[count] in op.object_dict.keys() or calc_string[count] == '(' or calc_string[count] == ')'):
            valid_calc_string.append(calc_string[count])
            
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    print(valid_calc_string)
    mathh = MathExpression()
    mathh.set_expression_from_string(valid_calc_string)
    clean_input(mathh.get_expression(), [])