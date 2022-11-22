import operations as op

def clean_input(calc_space_string):
    valid_calc_string = ""
    count_digit = 0
    count_operator = 0
    space = False
    for char in calc_space_string:
        match char:
            case ' ':
                space = True
                continue
            case '   ':
                space = True
                continue
            case _:
                if(char.isdigit()):
                    if(count_digit == 1 and space):
                        print("invalid input, there cannot be space between two numbers")
                        return
                    count_digit += 1
                    count_operator = 0
                    valid_calc_string += char
                    space = False
                    
                elif(char in op.OPERATIONS):
                    if(count_operator == 1 and char != '-'):
                        print("invalid input, too many operators")
                        return
                    count_digit = 0
                    count_operator += 1
                    valid_calc_string += char
                    space = False
                else:
                    print("invalid input")
                    return
    return valid_calc_string


if(__name__ == "__main__"):
    calc_string = input("please enter the equation: ")
    calc_string = clean_input(calc_string)
    print(calc_string)

