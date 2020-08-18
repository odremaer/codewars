#УЗНАЛ ПРО eval(expression, globals=None, locals=None)
def calculate(num1, operation, num2):
    try:
        return eval('{}{}{}'.format(num1,operation,num2))
    except(SyntaxError,ZeroDivisionError):
        return None


print(calculate(1,'+',2))