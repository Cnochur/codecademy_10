'''
10. Repeat the characters

Create a Python function that accepts a string. The function should return a string, with each character 
in the original string doubled. If you send the function “now” as a parameter, 
it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.
'''

def repeat_chars(string):

    chars_doubled =''.join([str(char * 2) for char in list(string)])

    return (chars_doubled)

print(repeat_chars('abc123!"£$'))

    