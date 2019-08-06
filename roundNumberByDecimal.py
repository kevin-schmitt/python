# round with two decimals
import math

def roundUp(number):
    return math.ceil( number / 10.0) * 10

def roundDown(number):
    return math.ceil( number // 10.0) * 10

print(roundDown(3.14159))
print(roundUp(3.14159))