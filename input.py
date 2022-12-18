def validation(num, validated_string = None):
    """This function validates the input of the user, if the input is valid, it will be sent to the first_cleaning function in the input.py file, if the input is invalid, the user will be asked to enter a valid input."""
    from Exceptions import InputError
    try:
        if(num == 1):
            if(validated_string == None):
                print("please enter a calculation")
                validated_string = input()
                if validated_string == "" or validated_string.isspace():
                    raise InputError("Invalid input, please enter a calculation, the string cannot be empty or only contain spaces/tabs")
                return validated_string
            else:
                if validated_string == "" or validated_string.isspace():
                    raise InputError("Invalid input, please enter a calculation, the string cannot be empty or only contain spaces/tabs")
                return validated_string
        else:
            print("the program has ended")
            exit(1)
    except KeyboardInterrupt as e:
        print("invalid input, only parenthesis, numbers and operations are allowed")
        from start import main
        main()
    except EOFError as e:
        print("invalid input, only parenthesis, numbers and operations are allowed")
        from start import main
        main()
    except InputError as e:
        print(e)
        from start import main
        main()
    pass