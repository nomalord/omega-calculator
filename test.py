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

#complex tests require a minimum of 20 characters, must include spaces, parenthesis, numbers, and operations
#the operations are: +, -, *, /, %, ^, ~, @, &, #, $, ~ as specified in the Operator.py file
#write me 20 tests for complex calculations

# Valid complex equations
def test_complex_equation_1():
    assert main("(3*(5-2)!)/((2!)/((-9^2)!)+10)") == 1.8

def test_complex_equation_2():
    assert main("((5&9)^(5^2$-4)- 3!)*-(-2@8!#!)") == -5.407303571701049e+22

def test_complex_equation_3():
    assert main("5!#^ 2 -(2^(-(2^2)@(2^3)))!") == -15.0

def test_complex_equation_4():
    assert main("((22/2)^3)#! - ~---120#!") == 40314.0

def test_complex_equation_5():
    assert main("(10*(5@15))%((25%4)^(2^2))") == 0.0

def test_complex_equation_6():
    assert main("((7!/6!)^2+5)- (40@((4*5)$69))") == -0.5

def test_complex_equation_7():
    assert main("(39%(4!/4)+2)^(~---2! + 2^3 - (4^2)/2)") == 25.0

def test_complex_equation_8():
    assert main("((7 *(8^2))/2)@(5*(((3^2)*2)/6))") == 119.5

def test_complex_equation_9():
    assert main("((7*8+2)#^-(-2&5)*2)*(5*2-4!#)") == 1352

def test_complex_equation_10():
    assert main("((2*2*2)*3!)-(((20^2)/2)/20)*6") == -12.0

def test_complex_equation_11():
    assert main("(4!/2^3)^2+2^((20+6@(2^3))/3^2)") == 17.0

def test_complex_equation_12():
    assert main("(6*3+1@(6^2/(2^2*3)))/(6!#-(8*5+1)#)") == 5.0

def test_complex_equation_13():
    assert main("(11^2)%((10+1!#)*((5*2^1)&(5*2^2)))") == 11

def test_complex_equation_14():
    assert main("42%(6!#-(2^2*2^3+10)%(2^3+5&12))") == 0

def test_complex_equation_15():
    assert main("-(2^3)*(5!#+3)+((5^2*2^2)/10+~---4)") == -34.0

def test_complex_equation_16():
    assert main("-((5+5+150%(40*3))*2@3)-(7*2^(11%(2^1*2^2)))") == -156.0

def test_complex_equation_17():
    assert main("-((10$4*3)*2^2+(25%(3*5)))+(20-(2^2)@(2*3))") == -115.0

def test_complex_equation_18():
    assert main("(30$14)*120#+2^(2&10)-(0.5+1/(16%((5!+1)/11)))") == 93.3

def test_complex_equation_19():
    assert main("50*(0.04*10^2)+3-2^(~--5@(10+(10*10)#))") == 195.0

def test_complex_equation_20():
    assert main("((10+10+10+3^2)/5!#)^2-(0.5*(2^-(-2&2)))") == 167.0

complex_test_list = [test_complex_equation_1, test_complex_equation_2, test_complex_equation_3, test_complex_equation_4,
                        test_complex_equation_5, test_complex_equation_6, test_complex_equation_7, test_complex_equation_8,
                        test_complex_equation_9, test_complex_equation_10, test_complex_equation_11, test_complex_equation_12,
                        test_complex_equation_13, test_complex_equation_14, test_complex_equation_15, test_complex_equation_16,
                        test_complex_equation_17, test_complex_equation_18, test_complex_equation_19, test_complex_equation_20]

i= 0
for test in complex_test_list:
    i += 1
    print(str(i) + " passed")
    test()
