Num_1 = int(input("Please Enter the first number: "))
Num_2 = int(input("Please Enter the second number: "))
Num_3 = int(input("Please Enter the third number: "))

if (Num_1 >= Num_2 and Num_1<=Num_3) or (Num_1 >= Num_3 and Num_1 <= Num_2) : 
    print (f'The median number is {Num_1}')
elif (Num_2 >= Num_1 and Num_2<=Num_3) or (Num_2 >= Num_3 and Num_2 <= Num_1) : 
    print (f'The median number is {Num_2}')
else : 
    print (f' The median number is {Num_3}')