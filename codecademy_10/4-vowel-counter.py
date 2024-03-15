'''
4. Count the vowels in a string

Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.
'''

def vowel_counter(word):

    vowel_counter = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    char_list = list(word)

    for letter in char_list:
        for vowel in vowel_list:
            if letter == vowel:
                vowel_counter += 1
        
    return vowel_counter

print(vowel_counter('america'))

