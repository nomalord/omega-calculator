# omega-calculator

start.py:
in order to run the project, go to the start.py module and run it.

input.py:
the input module checks whether the initial input is correct, ie it is not empty or only filled with whitespaces. also checks to see if the user made a keyboard interrupt
or anything of that sort and restarts the program.

validation_input.py:
this module checks the validity of the characters entered as input and clears all white spaces from the input.

MathExpression.py
this module is meant to create the blueprint for the MathExpression object, an object which defines the equation for later use. the MathExpression object contains in it
an "expression", "result", and "negative" fields. the expression is the equation itself, the result is the result of the equation and the negative field checks whether or
not the equation is negative. if there are parenthesis in the equation, the equation inside the parenthesis wiil become a MathExpression in itself.

Operator.py:
contains all the Operator objects: PairOperator, RightOperator, and LeftOperator. also in it are the operations themselves: add, subtract, divide, etc... defined as 
standalone functions. also in it are 2 dictionaries which are critical for the calculator to convert characters into object operators: object_dict - which contains
operator characters as keys, and instantiates them as Operator objects in their value, and function_dict - which contains operator characters as keys and has function
calls as the values for each key. this all ties into the ease of adding new operation into the calculator. all the user has to do is add the character of the operation
to the object_dict with the instantiation of that operator as its value (along with its priority and sign), create a new function to calculate the operation and add 
the operator as the key to the function_dict with the call to the function as its value. to decide what is the operator type, at the instantiation in the object_dict one
simply must choose between Pair, Right, or Left Operator and the calculator will be able to check the validity of the input later.

clean_equation.py:
contains the functions which check the validity of the Operator placements as well as cleaning extra minuses

Calculator.py:
contains the blueprint for the object Calculator which calculates the equations.

output.py:
outputs to the user the result and asks them whether they would like to continue using the calculator.

tests.py:
checks the calculator using the pytest library.
