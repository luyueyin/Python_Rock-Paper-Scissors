from images import logo, menu_image, you
import random
from charset_normalizer import from_path
import os
clear = lambda: os.system("clear")
from images import rock, paper, scissors, line
import getpass



images = [rock, paper, scissors]
user_score = 0
computer_score = 0


# make the game repeatable
while user_score < 3 and computer_score < 3:

    # ask user for a choice
    user_choice = int(input("1. Rock\n2. Paper\n3. Scissors\n\nWhat do you choose?\n"))

    #clear the screen between rounds.
    clear()
    if user_choice > 3 or user_choice < 1:
        print("Ivalid input, please enter a valid number.\n")
    else:
        print(you)
        print(images[user_choice - 1])
        print('''
    ---- - -- - - - -- - -- - - -- - - -- - -- 
        ''')

        # generate a random choice for the computer
        computer_choice = random.randint(1,3)
        print(images[computer_choice - 1])

        # check who is the winer   
        # give feedback + core keeping
        if user_choice == 3 and computer_choice == 1:
            computer_score += 1
            print(f"You Lose!\nYour current score: {user_score}\ncomputer_score: {computer_score}\n\n")
        elif user_choice == 1 and computer_choice == 3:
            user_score += 1
            print(f"You Win!\nYou current score: {user_score}\ncomputer_score: {computer_score}\n\n")
        elif user_choice == computer_choice:
            print(f"It's a Deaw!\nYour current score: {user_score}\ncomputer_score: {computer_score}\n\n")
        elif user_choice > computer_choice:
            user_score += 1
            print(f"You Win!\nYou current score: {user_score}\ncomputer_score: {computer_score}\n\n")
        elif user_choice < computer_choice:
            computer_score += 1
            print(f"You Lose!\nYour current score: {user_score}\ncomputer_score: {computer_score}\n\n")

# if user goes to 3 then the game should stop and print "win"
if user_score == 3:
    print("user win !")

# if computer goes to 3 then the game should stop and print "lose"
else:
    print("computer win !")



    


