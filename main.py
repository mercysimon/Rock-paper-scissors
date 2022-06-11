from operator import truediv
import random


possible_options=["R","P","S"]
user_choice=str(input("Enter your choice: "))

print(type(user_choice))


       
computer_choice=random.choice(possible_options)

print(f"Player {user_choice} : CPU {computer_choice} .")

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "R":
    if computer_choice == "S":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif user_choice == "P":
    if computer_choice == "R":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif user_choice == "S":
    if computer_choice == "P":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")