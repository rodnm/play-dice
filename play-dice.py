import random
import webbrowser

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again.lower() in ("yes", "y", "si"):
    print("Here we just Play Dice!")
    print("The Values are :")
    
    dice1 = random.randint(min_val, max_val)
    dice2 = random.randint(min_val, max_val)
    
    print(dice1)
    print(dice2)
    
    if dice1 == 6 or dice2 == 6:
        webbrowser.open("https://youtu.be/na6bysYNuS0")
        print("WHATCHU DOING BRUH")
        print("GO OUT AND LIVE YOUR LIFE!")
    else:
        print("It's never too late, our journey's just begun!")
        print("Before giving in show them your best try!")
    roll_again = input("Roll again? ")
    
print("K. BYE!")
