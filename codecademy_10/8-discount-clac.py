'''
8. Give me the discount

Create a function in Python that accepts two parameters. 
The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. 
For example, if the price is 100 and the discount is 20, the function should return 80.
'''

def discount_calc(total_price, discount_given):

    discounted_amount = (total_price * discount_given) / 100
    discounted_price = total_price - discounted_amount

    return int(discounted_price)

print(discount_calc(90, 20))