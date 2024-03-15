'''
1. Convert radians into degrees

Write a function in Python that accepts one numeric parameter. 
This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.
'''

import math

def radian_to_degrees(radian):
    
    degrees = radian * 180/math.pi
    
    return degrees

print(radian_to_degrees(2))