import random


highscore = {}

while True:
    playagain = input("Play? y/n ")
    if playagain == "y":
        pass
    if playagain == "n":
        break
    username = input("What is your name? ")
    score = 0
    while True:
        headstails = random.randint(0,1)
        userguess = input("heads or tails ")
        if userguess == "heads":
            userheadstails = 1
        elif userguess == "tails":
            userheadstails = 0
        if headstails == userheadstails:
            score += 1
            print("Correct! Your score is: " + str(score))
        else:
            if (username in highscore) == False:
                highscore[username] = score

            elif (username in highscore) == True:
                if highscore[username] < score:
                    highscore[username] = score
                    
            print("\n you lose! \n")
            for key, val in highscore.items():
                print("Username: " + key + "\tHighscore: " + str(val))
            break
