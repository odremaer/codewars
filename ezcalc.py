def calculate(num1, operation, num2):
        oper = ['+','-','*','/']
        try:
            if operation in oper:
                if operation == '+':
                    return num1 + num2
                if operation == '-':
                    return num1 - num2
                if operation == '/':
                    return num1 / num2
                if operation == '*':
                    return num1 * num2
            else:
                return None
        except ZeroDivisionError:
            return None

print(calculate(3.2,'+', 8))