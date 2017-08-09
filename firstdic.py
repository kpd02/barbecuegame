dictionary = {
    "hello" : {
        "French" : "bonjour",
        "Spanish" : "hola",
        "German" : "hallo"
    },
    "goodbye" : {
        "French" : "au revoir",
        "Spanish" : "adois",
        "German" : "auf Wiedersehen"
    },
    "yes" : {
        "French" : "oui",
        "Spanish" : "si",
        "German" : "ja"
    },
    "goodnight" : {
        "French" : "bonne nuit",
        "Spanish" : "buenas noches",
        "German" : "gute Nacht"
    }
}

for key in dictionary:
    print(key)
engword = input("Type the word you want to translate: ")
tolang = input("Translate to French/Spanish/German: ")
whichword = dictionary[engword]
translation = whichword[tolang]
print(translation)
