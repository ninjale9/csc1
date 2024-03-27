phone_num = int(input('Please enter your phone number:'))

line_number= phone_num % 10000
phone_num = phone_num // 10000

prefix= phone_num%1000
phone_num= phone_num//1000

area_code= -phone_num

print('(',area_code,')' '' ,prefix,'-',line_number,)