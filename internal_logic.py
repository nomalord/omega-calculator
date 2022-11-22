import operations as op

def check_input(input:str):
    for char in input:
        if(char.isdigit()):
            num1 = int(char)
        elif(char == ' ' or char == '   '):
            continue
        

def check_op(char):
    if(char not in op.OPERATIONS):
        print("Invalid input.")
    else:
        print("valid input.")