def add(num_1, num_2) :
    return num_1 + num_2 

def substract (num_1 , num_2) :
    return num_1 - num_2

def multiply (num_1, num_2) :
    return num_1 * num_2

def divide (num_1, num_2) :
    if num_2 != 0 :
        return num_1 / num_2
    else: 
        return "Error: Divison by zero " 

def power (num_1, num_2) :
    return num_1 ** num_2 

def floor_divide (num_1, num_2) :
    if num_2 != 0 :
        return num_1 // num_2 
    else :
        return "Error: Floor Divison by zero"

def modulus (num_1, num_2) :
    if num_2 != 0 :
        return num_1 % num_2
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
    "**": power,
    "//" : floor_divide,
    "%" : modulus,
}

while True :
    calculator_input = (input(".> "))
    if calculator_input.lower()=="quit" or calculator_input.lower () =="q":
        break 
    parts = calculator_input.split()
    expression = " ".join(parts) 
    if len(parts) != 3 :
        print(f"Error: invalid input format --> ({expression})")
        continue
    num_1 = float(parts[0])
    operator = parts[1] 
    num_2 = float(parts[2])
    if operator not in operations : 
        print (f"Error : Invalid operator --> ({expression})")
        continue
    results = operations[operator](num_1,num_2)
    print (f"Results : {expression} = {results}")