def text_filter (txt) :
    str_input= message 
    word_banned = ['Turkey','Dog', "Fox", 'Cat', "Chicken"]

    string_list = str_input.split()
    string_list2= []

    for i in string_list : 
        if i not in word_banned:
            string_list2.append(i)
    txt= " ".join(string_list2)
    return txt 
message= input("Please enter your message: ")
print (f'Input Message : {message}')
print(f'Out Messages : {text_filter(message)}')
