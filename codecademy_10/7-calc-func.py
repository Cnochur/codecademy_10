'''
7. Create a calculator function

Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or . 
The third parameter will also be an integer.

The function should perform a calculation and return the results. 
For example, if the function is passed 6 and 4, it should return 24.
'''

def calculator_func(x, operator, y):

    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '/':
        if x == 0 or y == 0:
            return('Cannot divide by 0')
            quit()
        else:
            return x // y
    elif operator == '*':
        return x * y
    

print(calculator_func(10, '/', 5))