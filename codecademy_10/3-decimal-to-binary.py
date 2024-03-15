'''
3. Convert a decimal number into binary

Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
To make this simple, the decimal number will always be less than 1,024, 
so the binary number returned will always be less than ten digits long.
'''

def decimal_to_binary(decimal):

    binary = ''

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
        
    return binary.zfill(4)

print(decimal_to_binary(13))
