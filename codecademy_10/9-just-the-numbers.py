'''
9. Just the numbers

Write a function in Python that accepts a list of any length that contains 
a mix of non-negative integers and strings. The function should return a list 
with only the integers in the original list in the same order.
'''

def just_the_nums(random_values_list):
    nums_list = []

    for value in random_values_list:
        if value != str(value):
            nums_list.append(value)

    return nums_list


val_list = [-1, 'nan', -13, -21, 'nan', -100, 23, -33, 'nan', 'nan']

print(just_the_nums(val_list))