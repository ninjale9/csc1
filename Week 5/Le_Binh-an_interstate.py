highway_num = int(input('Please enter an interstate number: '))
serve_num= highway_num % 100

if 1<= highway_num <=99 :  
    print (f'{highway_num} is a valid interstate highway number')
    if  (highway_num % 2) == 0 :
        print (f'I-{highway_num} is a primary , going east / west ')
    else : 
        print (f'I-{highway_num} is a primary , going north/south ') 
elif 100<= highway_num <= 999 :  
    if highway_num % 100 == 0:
        print (f'{highway_num} is not a valid interstate number')
    elif highway_num % 2 == 0 : 
        print (f'I-{highway_num} is auxiliary , servicing I-{serve_num}, going east/ west')
    else :
        print (f'I-{highway_num} is auxiliary , servicing I-{serve_num}, going north/ south')
else : 
    print (f'{highway_num} is not a valid interstate number ')