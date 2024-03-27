age= int(input('Please enter your age: '))
if age <= 13 : 
    print ('You are in the child age group and receive a 20% discount')
elif 13<= age <= 19 :
    print ('You are in the teenager age group and receive a 10% discount')
elif 20<= age <= 64 : 
    print ('You are in the Adult age group and receive a 5% discount')
elif age >= 65 :
     print ('You are in the Senior age group and receive a 15% discount')
