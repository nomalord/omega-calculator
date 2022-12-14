
def validation():
    try:
        if input() == "":
            print("Invalid input, please enter a calculation")
            return
    except KeyboardInterrupt as e:
        print(e)
        print("please enter a calculation")
    finally:
        validation()
        

while(True):
    print("please enter a calculation")
    validation()