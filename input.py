def validation(num):
    """This function validates the input of the user, if the input is valid, it will be sent to the first_cleaning function in the input.py file, if the input is invalid, the user will be asked to enter a valid input."""
    import validation_input as inp
    try:
        print("please enter a calculation")
        if(num == 1):
            validated_string = input()
            if validated_string == "" or validated_string.isspace():
                print("Invalid input, please enter a calculation, the string cannot be empty or only contain spaces/tabs")
                validation(1)
            inp.first_cleaning(validated_string, [])
        else:
            print("the program has ended")
            exit(1)
    except KeyboardInterrupt as e:
        print(e)
        validation(1)
    pass