import operations as op

def clean_input(calc_space_string):
    """Removes spaces and tabs from the input string and check"""
    count = 0
    valid_calc_string = []
    for char in calc_space_string:
        match char:
            case ' ':
                pass
            case '\t':
                pass
            case _:
                if(char.isdigit()):
                    if(check_digit_parenth(calc_space_string[count+1:])):
                        valid_calc_string.append(char)
                    else:
                        print("Invalid input, there cannot be an opening parenthesis after a digit")
                        print("or a closing parenthesis before a digit")
                        return
                elif(char in op.operation_object.keys() or char == '(' or char == ')'):
                    if(space_check_operation(calc_space_string[count+1:], char)):
                        print("Invalid input, there cannot be two operations next to each other")
                        return
                    else:
                        for key in op.operation_object:
                            if(char == op.operation_object[key].operator):
                                valid_calc_string.append(op.operation_object[key])
                else:
                    print("invalid input, only parenthesis, numbers and operations are allowed")
                    return
        count += 1
    return valid_calc_string

def check_digit_parenth(string_digit_check):
    """Checks if there is a parenthesis after a digit, returns false if there is"""
    for char in string_digit_check:
        match char:
            case '(':
                return False
            case ' ':
                pass
            case '\t':
                pass
            case _:
                return True
    pass


def space_check_operation(string_operation_check, og_char):
    """Checks if there are two operations back to back, returns false if they are not or if operator is -"""
    for char in string_operation_check:
        match char:
            case ' ':
                pass
            case '\t':
                pass
            case _:
                if(char in op.operation_object.keys()):
                    match char:
                        case '-':
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
    print(clean_input(string_calc))