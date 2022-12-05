import operations as op

def clean_input(calc_space_string):
    count = 0
    valid_calc_string = ""
    for char in calc_space_string:
        match char:
            case ' ':
                pass
            case '\t':
                pass
            case _:
                if(char.isdigit()):
                    valid_calc_string += char
                elif(char in op.OPERATIONS):
                    if(space_check_operation(calc_space_string[count+1:], char)):
                        print("Invalid input, there cannot be two operations next to each other")
                        return
                    else:
                        valid_calc_string += char
                else:
                    print("invalid input")
                    return
        count += 1
    return valid_calc_string

# def space_check_digit(string_digit_check):
#     """Checks if there is a space between two digits, returns false if there is not"""
#     space = False
#     for char in string_digit_check:
#         match char:
#             case ' ':
#                 space = True
#                 continue
#             case '\t':
#                 space = True
#                 continue
#             case _:
#                 if(char.isdigit() and space):
#                     return True
#                 else:
#                     return False

def space_check_operation(string_operation_check, og_char):
    """Checks if there is a space between two operations, returns false if there is not or if operator is -"""
    count = 0
    for char in string_operation_check:
        match char:
            case ' ':
                pass
            case '\t':
                pass
            case _:
                if(char in op.OPERATIONS):
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
        count += 1



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