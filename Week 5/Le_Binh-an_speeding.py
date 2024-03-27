Speed_limit = float(input("Please enter the speed limit for the road: "))
Vehicle_speed = float(input("Please enter the vehicle's recorded speed: "))
Diff_speed = Vehicle_speed - Speed_limit

if Diff_speed <= -10:
    print('The speeding fine is $50 ')
elif 6 <= Diff_speed <= 20:
    print('The speeding fine is $75 ')
elif 21 <= Diff_speed <= 40: 
    print('The speeding fine is $150 ')
elif Diff_speed >= 41:
    print ('The speeding fine is $300 ')
else :
    print ('There is no ticket ')