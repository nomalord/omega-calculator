# Description: This is the main file of the project. It is used to run the project.
def main(string = None, test = False):

    if(test):
        exit()

    from input import validation
    import validation_input as inp
    from MathExpression import MathExpression
    from clean_equation import wrap_try
    from Calculator import Calculator

    validated_string = validation(1, string, test_check=test)
    validated_string = inp.first_cleaning(validated_string, [], test_check=test)

    math_expression = MathExpression()
    math_expression.set_expression_from_string(validated_string, test_check=test)

    validated_string = wrap_try(math_expression.get_expression(), test_check = True)
    math_expression.set_expression(validated_string)
    math_expression.parenthesis_checker()
    calculator = Calculator(math_expression.get_expression())
    math_expression.result = calculator.evaluate(calculator.expression)

    if(string == None):
        from output import output
        output(math_expression.result)
        
    return math_expression.result


if __name__ == "__main__":
    main()
