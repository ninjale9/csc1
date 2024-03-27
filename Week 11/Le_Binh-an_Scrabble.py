def scrabble_dict () :
    scrabble_values =  {
"A" : 1, "B" : 3, "C" : 3, "D" : 2,
"E" : 1, "F" : 4, "G" : 2, "H" : 4,
"I" : 1, "J" : 8, "K" : 5, "L" : 1,
"M" : 3, "N" : 1, "O" : 1, "P" : 3,
"Q" : 10,"R" : 1, "S" : 1, "T" : 1,
"U" : 1, "V" : 4, "W" : 4, "X" : 8,
"Y" : 4, "Z" : 10, 
    }
    while True : 
        word_game = input(":> ").upper()

        if word_game.upper() == "QUIT" or word_game.upper() == "Q" :
            break 

        word_value = 0

        for alphabets in word_game: 
            if  alphabets in scrabble_values:
                word_value += scrabble_values[alphabets]
        print(f'{word_game} is worth {word_value} points')


scrabble_dict()