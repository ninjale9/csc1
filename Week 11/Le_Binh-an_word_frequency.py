def build_dictonary () : 
    word_count = {}
    sentence = input("Please enter your sentence: ").lower()
    word_sorting = sentence.split()
    
    for word in word_sorting :
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1
    for word , count in word_count.items():
        print (f"{word} - {count}")
build_dictonary()
