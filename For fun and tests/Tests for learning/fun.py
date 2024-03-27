active = True
while active:
    message = input('Tell me something cool: ')
    if message == "quit":
        active = False
    else:
        print(message)