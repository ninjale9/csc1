import math

line_a= float(input("Please enter the length of side A of the triangle (in meters): "))
line_b= float(input("Please enter the length of side B of the triangle (in meters): "))
line_c= float(input("Please enter the length of side C of the triangle (in meters): "))

perimeter= ((line_a + line_b + line_c))
print(f'The perimeter of the triangle is {perimeter}m')

semi_per= (.5*(line_a + line_b + line_c))

area= math.sqrt(semi_per*(semi_per - line_a)*(semi_per - line_b)*(semi_per - line_c))
print(f'The area of the triangle is {area}')

side_add= line_a**2 + line_b**2

if side_add == line_c**2 :
    print('Your triangle is a Right triangle') 
elif side_add > line_c**2 :
    print('Your triangle is a Acute triangle')
elif side_add < line_c**2 :
    print('Your triangle is an Obtuse triangle')