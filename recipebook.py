import ast
#function to view pantry
def viewPantry():
    print("YOUR CURRENT PANTRY:")
    for key, val in pantry.items():
        strtoprint = "{:<20}{:<20}".format(key, str(val))
        print(strtoprint)
    print("\n")

#function to view shop
def viewShop():
    print("WELCOME TO THE STORE")
    for key, val in shop.items():
        strtoprint = "{:<20}{:<20}".format(key, str(val))
        print(strtoprint)
    print("\n")

#function to view recipe book
def viewRecipe():
    print("RECIPE BOOK\n")
    for item in recipe:                                                                         #goes through every item of the first dictionary
        print("Event: " + item)
        seconddic = recipe[item]                                                                #set variable that creates new dictionary without first item
        for key, val in seconddic.items():
            strtoprint = "{:<40}{:<20}".format("Ingredient: " + key, "Amount: " + str(val))     #now prints everything in the new dictionary
            print(strtoprint)
        print("\n")
    print("\n")

#Views the shop, then takes user input and adds that to the pantry
def buy(initmoney):
    viewShop()
    itembought = input("Which item do you want to buy? ")
    amount = input("How much of the item? ")
    amount = int(amount)
    if (itembought in pantry) == True:                                          #Adds to the value if the item already exists
        pantry[itembought] += amount
    else:                                                                       #initializes a new item in the pantry if it doesn't already exist
        pantry[itembought] = amount
    print("\n")
    viewPantry()
    moneylost = shop[itembought] * amount                                       #variable for the value of the dictionary, multiplied by the amount of item
    initmoney = initmoney - moneylost
    return initmoney                                                            #returns something, so money in the main code can be set to whatever after bought

#takes user input for what you want to sell, and then removes from pantry
def sell(initmoney):
    viewPantry()
    itemsell = input("Which item do you want to sell? ")
    amount = input("How much of the item do you want to sell? ")
    amount = int(amount)
    if (itemsell in pantry) == True:                                            #checks to see if the item is already in the pantry, then subtracts from value of the pantry dictionary
        pantry[itemsell] -= amount
        if pantry[itemsell] <= 0:
            del pantry[itemsell]
    else:
        print("You do not have any of this item")
    print("\n")
    viewPantry()
    multamount = shop[itemsell] * amount                                        #now subtracts money based on amount, and returns a variable to use with money
    initmoney = initmoney + multamount
    return initmoney

#takes user input to make an item from the pantry
def make():
    viewRecipe()
    viewPantry()
    eventcreate = input("Which event do you want to create? ")
    event = recipe[eventcreate]
    for ingredient in event:
        if (ingredient in pantry) == False:
            print("You do not have any " + ingredient)
        elif pantry[ingredient] == 0:
            print("You do not have enough" + ingredient + "to create this event")
        else:
            tosubtract = event[ingredient]
            pantry[ingredient] -= tosubtract
            if pantry[ingredient] == 0:
                del pantry[ingredient]
    pantry[eventcreate] = 1
    print("\n")
    viewPantry()

#what user command prints
def userCommand():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nPress \t'p' to view Pantry\nPress \t's' to view Store\nPress \t'r' to view Recipe Book\nPress \t'b' to buy from Store\nPress \t'ss' to sell stuff from Pantry\nPress \t'm' to make a new item\nPress any key to exit")

#initialize money and pantry when the file is opened
def initmoney(initmoney):
    monread = open("moneysaved.txt", "r")
    initmoney = monread.readline()
    monread.close()
    initmoney = int(initmoney)
    print("\nYour money is: " + str(initmoney))
    return initmoney

def initpantry(initpantry):
    with open("pantry.txt", "r") as data:
        initpantry = ast.literal_eval(data.read())
    return initpantry

#closes and saves the new values for money and pantry
def save():
    pantry = str(pantry)
    pantrywrite = open("pantry.txt", "w")
    pantrywrite.write(pantry)
    pantrywrite.close()
    monwrite = open("moneysaved.txt", "w")
    monwrite.write(str(money))
    monwrite.close()

#initialize pantry dictionary
pantry = {}

#shop dictionary (all of the items available to buy plus their value)
shop = {
    "Casual Barbecue" : 50,
    "Family Grill" : 40,
    "Work Party" : 20,
    "ground hamburger" : 3,
    "buns" : 3,
    "toppings" : 2,
    "steak" : 4,
    "bratwurst" : 4,
    "fancy mustard" : 4,
    "corn" : 2,
    "grilled veggies" : 2,
    "barbecue sauce" : 2,
    "good buds" : 7,
    "patience" : 7,
    "hot dogs" : 2,
    "cold blood" : 7,
    "growth mindset" : 7
}

#dictionaries that map ingredients to their amounts
casual = {
    "ground hamburger" : 2,
    "buns" : 2,
    "toppings" : 2,
    "corn" : 2,
    "good buds" : 1
}
grill = {
    "hot dogs" : 2,
    "ground hamburger" : 2,
    "buns" : 4,
    "grilled veggies" : 1,
    "patience" : 1
}
party = {
    "bratwurst" : 2,
    "fancy mustard" : 1,
    "grilled veggies" : 1,
    "cold blood" : 1,
    "growth mindset" : 1
}
#recipe book (name of the finished product which maps to the dictionary with ingredients and their amounts)
recipe = {
    "Casual Barbecue" : casual,
    "Family Grill" : grill,
    "Work Party" : party
}

money = 0
money = initmoney(money)
pantry = initpantry(pantry)
viewPantry()
while True:
    userCommand()
    print("\n")
    command = input("What do you choose? ")
    print("\n")
    if command == "p":
        viewPantry()
    elif command == "s":
        viewShop()
    elif command == "r":
        viewRecipe()
    elif command == "b":
        money = buy(money)
        print("Money: " + str(money))
        print("\n")
    elif command == "ss":
        money = sell(money)
        print("Money: " + str(money))
        print("\n")
    elif command == "m":
        make()
    else:
        break
pantry = str(pantry)
pantrywrite = open("pantry.txt", "w")
pantrywrite.write(pantry)
pantrywrite.close()
monwrite = open("moneysaved.txt", "w")
monwrite.write(str(money))
monwrite.close()
