import math
import random
# calculating the volume of a sphere
radius= int(input("Please enter the radius of the sphere: "))
volume= (4/3)*math.pi*math.pow(radius,3)
print(f'The volume of a sphere that has this number {radius} as a radius,has a volume of ", {volume:.2f}')

test = random.randint(1,10)
print(f'The factorial of {test} is {math.factorial(test)}')
