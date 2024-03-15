'''
2. Sort a list

Create a function in Python that accepts two parameters. The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. 
If it’s “desc,” then the list should be in descending order, and if it’s “none,” 
it should return the original list unaltered.
'''

def sort_list(num_list, order):

    if order.lower() == 'none':
        return num_list
    elif order.lower() == 'asc':
        num_list = sorted(num_list)
        return num_list
    elif order.lower() == 'desc':
        num_list = sorted(num_list, reverse = True)
        return num_list

age_list = [23, 12, 2, 9, 4, 32]

sorted_list = sort_list(age_list, 'desc')
print(sorted_list)