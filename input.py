import operations as op
from clean_equation import clean_input
from MathExpression import MathExpression

def first_cleaning(calc_string, valid_calc_string):
    """Removes spaces and tabs from the input string and checks for invalid characters"""

    calc_string = calc_string.replace(" ", "")
    calc_string = calc_string.replace("\t", "")
    for count in range(len(calc_string)):
        if(calc_string[count].isdigit()):
            # if(check_digit_parenth(calc_string[count+1:])):
            valid_calc_string.append(calc_string[count])
            # else:
            #     print("Invalid input, there cannot be an opening parenthesis after a digit")
            #     print("or a closing parenthesis before a digit")
            #     return
        elif(calc_string[count] in op.operation_object.keys() or calc_string[count] == '(' or calc_string[count] == ')'):

            # if(check_operation(calc_string[count+1:], calc_string[count], num_check_before_minus)):
            #     print("Invalid input, there cannot be two operations next to each other that are"+
            #     "not minuses or an operation next to a minus without a number or bracket before it")
            #     return
            # else:
            valid_calc_string.append(calc_string[count])
            
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    print(valid_calc_string)
    mathh = MathExpression()
    mathh.set_expression_from_string(valid_calc_string)
    clean_input(mathh.get_expression(), [])


if __name__ == "__main__":
    string_calc = input("Please enter a calculation: ")
    first_cleaning(string_calc, [])