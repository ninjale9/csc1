phone_number = int(input('Please enter your phone number: '))
areacode = phone_number // 10000000

prefix_number = phone_number // 10000 % 1000
line_number = phone_number % 10000

print("({}) {}-{}".format(areacode, prefix_number, line_number))