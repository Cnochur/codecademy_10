'''
6. Are the Xs equal to the Os?

Create a Python function that accepts a string. This function should count the number of Xs and 
the number of Os in the string. It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. 
If the count isn’t the same, it should return False. If there are no Xs or Os in the string, 
it should also return True because 0 equals 0. The string can contain any type and number of characters.
'''

def x_equal_o(string):

    equal = False
    x_counter = 0
    o_counter = 0

    new_string = list(string)

    while True:
        for letter in new_string:
            if letter.lower() == 'x':
                x_counter += 1
            elif letter.lower() == 'o':
                o_counter += 1
            else:
                break
    
        if x_counter == o_counter:
            equal = True
            return equal
        else:
            return equal
            


print(x_equal_o('xoxoxox'))