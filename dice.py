import random;

print("Welcome to the World's greatest dice roller!")
print("--------------------------------------------")

print("How many dice would you like to roll?")

### validate the input here
while True:
    try:
        numberPicked = int(input("Type an integar between 1 and 10: "))
        if(numberPicked > 0 and numberPicked < 10):
            break
        else:
            print("Invalid input. Try again please.")
    except:
        print("Please provide an integar")

def rollDice(amountOfDice):
    possibleFaces = [1,2,3,4,5,6]
    for die in range(amountOfDice):
        roll = random.choice(possibleFaces)
        print("Die ", die + 1, ": ", roll)


    
rollDice(numberPicked)