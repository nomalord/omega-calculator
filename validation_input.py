from input import first_cleaning

def validation():
    try:
        validated_string = input()
        if validated_string == "":
            print("Invalid input, please enter a calculation")
            return
        first_cleaning(validated_string, [])
    except KeyboardInterrupt as e:
        print(e)
        print("please enter a calculation")
        first_cleaning(validated_string, [])
    pass

def main():
    print("please enter a calculation")
    validation()

main()