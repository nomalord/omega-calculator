import pytest
from start import main
from Exceptions import OperatorError, InputError, ParenthesisError

def syntax_test1():
    with pytest.raises(OperatorError):
        main("27~&")

def syntax_test2():
    with pytest.raises(ParenthesisError):
        main("(27+3))")

def syntax_test3():
    with pytest.raises(OperatorError):
        main("27+3+")

def syntax_test4():
    with pytest.raises(OperatorError):
        main("@9~+3+^@")

def syntax_test5():
    with pytest.raises((OperatorError, ParenthesisError)):
        main("(2764737+3+^@(")

def gibberish_test():
    with pytest.raises(InputError):
        main("this is gibberish jq3tq3ljtjgb ^C")

def empty_string_test():
    with pytest.raises(InputError):
        main("")

def whitespace_test():
    with pytest.raises(InputError):
        main("       \t\t  \t \t")

def simple_calculation_test1():
    assert main("27+3") == 30

def simple_calculation_test2():
    assert main("27-3") == 24

def simple_calculation_test3():
    assert main("27*3") == 81

def simple_calculation_test4():
    assert main("27/3") == 9

def simple_calculation_test5():
    assert main("27%3") == 0

def simple_calculation_test6():
    assert main("27^3") == 19683

def simple_calculation_test7():
    assert main("27+3$4") == 31

def simple_calculation_test8():
    assert main("27@3*4") == 60

def simple_calculation_test9():
    assert main("27%3^4") == 0

def simple_calculation_test10():
    assert main("27+3&4") == 30

def simple_calculation_test11():
    assert main("(~27-3)*4") == -120

def simple_calculation_test12():
    assert main("5!*2") == 240

def simple_calculation_test13():
    assert main("(8&2)*7") == 14

def simple_calculation_test14():
    assert main("7@3$2 + 928#   ") == 24

def simple_calculation_test15():
    assert main("80@2&50%10 + -~-928#") == -18

simple_test_list = [simple_calculation_test1, simple_calculation_test2, simple_calculation_test3, simple_calculation_test4,
                    simple_calculation_test5, simple_calculation_test6, simple_calculation_test7,
                    simple_calculation_test8, simple_calculation_test9, simple_calculation_test10,
                    simple_calculation_test11, simple_calculation_test12, simple_calculation_test13,
                    simple_calculation_test14, simple_calculation_test15]

for test in simple_test_list:
    test()

#complex tests require a minimum of 20 characters, must include spaces, parenthesis, numbers, and operations
#the operations are: +, -, *, /, %, ^, ~, @, &, #, $, ~ as specified in the Operator.py file
#write me 20 tests for complex calculations

def complex_calculation_test1():
    pass


# + : addition, priority 1, takes 2 arguments
# - : subtraction , priority 1 , takes 2 arguments
# * : multiplication , priority 2 , takes 2 arguments
# / : division , priority 2 , takes 2 arguments
# ^ : exponentiation , priority 3 , takes 2 arguments
# % : modulo , priority 4 , takes 2 arguments
# @ : average , priority 5 , takes 2 arguments
# $ : maximum , priority 5 , takes 2 arguments
# & : minimum , priority 5 , takes 2 arguments
# ! : factorial , priority 6 , takes 1 argument, right from the number
# ~ : negative, priority 6 , takes 1 argument, left from the number
# # : sum , priority 6 , takes 1 argument, left from the number
