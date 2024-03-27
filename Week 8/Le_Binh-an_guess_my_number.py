import random 
def num_game () : 
    The_Num= random.randint(0,100) 
    attempts = 0
    print("I have generated a random number between 1 and 100. You will have 10 attempts to guess the number  ")
    while attempts < 10 : 
        User_Input= int(input("Please enter your guess for the number: "))   
        attempts += 1
        if User_Input > The_Num:
                print (f'Your Guess is greater than my random number. Try Again. \nGuess {attempts}')   
        elif User_Input < The_Num :
            print (f'Your Guess is less than my random number. Try Again \nGuess {attempts}')
        else :
            print(f'You guessed the correct number, congrats ')
            break
    else :
            print (f' You have run out of attempts, The correct number was {The_Num}')
num_game()