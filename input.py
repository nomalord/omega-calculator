import operations as op
from MathExpression import MathExpression

def clean_input(calc_string, valid_calc_string):
    """Removes spaces and tabs from the input string and check"""

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

            num_check_before_minus = calc_string[count] == '-' and (count == 0 or calc_string[count-1].isdigit() 
            or calc_string[count-1] == ')' or calc_string[count-1] == '(')

            # if(check_operation(calc_string[count+1:], calc_string[count], num_check_before_minus)):
            #     print("Invalid input, there cannot be two operations next to each other that are"+
            #     "not minuses or an operation next to a minus without a number or bracket before it")
            #     return
            # else:
            if(calc_string[count] == '-'):
                toupleCheck = minus_clean(calc_string[count:])
                if(toupleCheck[0] == '+'):
                    if(calc_string[toupleCheck[1]+count].isdigit() and count != 0 and
                        calc_string[count-1] != '(' and calc_string[count-1] != '+'): 
                        valid_calc_string.append('+')
                    clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)
                    return
                if(count == 0 or calc_string[toupleCheck[1]+count].isdigit() or calc_string[count-1] == ')'):
                    if(calc_string[toupleCheck[1]+count].isdigit()):
                        valid_calc_string.append('-'+calc_string[toupleCheck[1]+count])
                        clean_input(calc_string[toupleCheck[1]+count+1:], valid_calc_string)
                        return
                valid_calc_string.append(toupleCheck[0])
                clean_input(calc_string[toupleCheck[1]+count:], valid_calc_string)
                return
            else:
                valid_calc_string.append(calc_string[count])
        else:
            print("invalid input, only parenthesis, numbers and operations are allowed")
            return
    plus_removal(valid_calc_string)

    print(valid_calc_string)
    # mathh = MathExpression()
    # mathh.set_expression_from_string(valid_calc_string)
    # if(not mathh.left_right_operator_check()):
    #     return
    # mathh.parenthesis_checker()
    # mathh.sort_expression()
    # print()



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

def plus_removal(valid_calc_string):
    for item in range(len(valid_calc_string)-1):
        if(valid_calc_string[item] == '+'):
            if(valid_calc_string[item+1] == '-'): del valid_calc_string[item]


if __name__ == "__main__":
    string_calc = input("Please enter a calculation: ")
    clean_input(string_calc, [])