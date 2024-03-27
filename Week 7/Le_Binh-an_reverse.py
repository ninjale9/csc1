s= input('Please enter your string: ')
t= "Reversed: "
while s not in {"quit", "Quit", "q"} :
    print(t+s[::-1])
    s=input()