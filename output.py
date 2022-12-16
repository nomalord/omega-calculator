def output(result):
    """Prints the result of the calculation"""
    from input import validation
    print("--------------------")
    if(type(result) == float):
        float_str = str(result)
        decimal_index = float_str.index('.')
        first_number_after_point = float_str[decimal_index + 1]
        second_number_after_point = float_str[decimal_index + 2]
        if(first_number_after_point == '0' and second_number_after_point == '0'):
            print("the result is " + str(int(result)))
        else:
            print("the result is " + str(result))
    else:
        print("the result is " + str(result))
    print("--------------------")
    print("if you would like to do another calculation, type 'y' or 'yes'")
    print("if you would like to exit, type 'n' or 'no'")
    print("--------------------")
    while True:
        try:
            answer = input()
            if(answer == "y" or answer == "yes"):
                validation(1)
            elif(answer == "n" or answer == "no"):
                print("the program has ended")
                exit(1)
            else:
                print("Invalid input, please enter 'y' or 'yes' to do another calculation or 'n' or 'no' to exit")
        except KeyboardInterrupt as e:
            print(e)
            print("please enter 'y' or 'yes' to do another calculation or 'n' or 'no' to exit")
            continue
    pass