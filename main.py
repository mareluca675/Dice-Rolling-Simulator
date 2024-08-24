import random

print("Do you want to roll a dice?")
answer = (input()).lower()
playAgain = True

while(answer != "yes" and answer != "no"):
    print("Please enter either 'yes' or 'no'.")
    answer = (input()).lower()

while playAgain == True:
    if answer == "yes":
        dice_roll = random.randint(1, 6)
        if(dice_roll == 1):
            print("+-------+")
            print("|       |")
            print("|   o   |")
            print("|       |")
            print("+-------+")
        elif (dice_roll == 2):
            print("+-------+")
            print("|       |")
            print("| o   o |")
            print("|       |")
            print("+-------+")
        elif (dice_roll == 3):
            print("+-------+")
            print("| o     |")
            print("|   o   |")
            print("|     o |")
            print("+-------+")
        elif (dice_roll == 1):
            print("+-------+")
            print("| o   o |")
            print("|       |")
            print("| o   o |")
            print("+-------+")
        elif (dice_roll == 1):
            print("+-------+")
            print("| o   o |")
            print("|   o   |")
            print("| o   o |")
            print("+-------+")
        else:
            print("+-------+")
            print("| o   o |")
            print("| o   o |")
            print("| o   o |")
            print("+-------+")

        print(f"You rolled a {dice_roll}!")
        print("Would you like to roll again?")
        answer = (input()).lower()

        while (answer != "yes" and answer != "no"):
            print("Please enter either 'yes' or 'no'.")
            answer = (input()).lower()

        if answer == "yes":
            playAgain = True
        else:
            playAgain = False
    else:
        playAgain = False
print("Too bad.")