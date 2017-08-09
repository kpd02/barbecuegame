def letterinword (word):
    dictionary = {}
    for letter in word:
        if (letter in dictionary) == False:
            dictionary[letter] = 1
        elif (letter in dictionary) == True:
            dictionary[letter] += 1
    return dictionary


word1 = input("type a word: ")
call = letterinword(word1)
for key, val in call.items():
    print("Character: " + key + "\tTimes Appearing: " + str(val))
