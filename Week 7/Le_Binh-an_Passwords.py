password = input('Please enter your password: ')
new_letter = {
    "o" : "0" ,
    "i" : "1" , 
    "a" :  "@"   , 
    "e" :  "3" ,
    "A" :  "4" ,
    "B" :  "8" ,
    "s" :  "$" ,
}
password = list(password)

for index , item in enumerate(password): 
    for key, value in new_letter.items():
        if item==key: 
            password[index]= value 

print("".join(password)+"!")