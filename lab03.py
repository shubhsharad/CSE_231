word = input("Enter your word: ").lower()
#print(word)
vowels ="aeiou"
while word != "quit":
    if word[0] in vowels:
        print(word+"way")
    else:
        for i in range(0,len(word)):
            if word[i] in vowels:
                c = word[0:i]
                new_word = word.replace(c,"")
                #print(new_word)
                print(new_word+c+"ay")
                break
    word = input("enter your word: ").lower()