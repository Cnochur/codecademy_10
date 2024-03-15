'''
5. Hide the credit card number

Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
'''

def hide_card_num(card_number):

    new_list = list(str(card_number))
    last_four = new_list[-4:]

    last_four_string = ''.join(last_four)
    hidden_num = '****-****-****-' + last_four_string

    return hidden_num

print(hide_card_num(12345676))
