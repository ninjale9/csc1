Values= int(input('Please enter the number of floating-point values:'))
values_in_list= []
for i in range (Values):
    num_list= float(input(f'Enter number{i+1}: '))
    values_in_list.append(num_list)

divisor= max(values_in_list)

New_list= [x / divisor for x in values_in_list]

print('Normalized Floating-Point Values: ')
for f in New_list:
    print('{:.2f}'.format(f))