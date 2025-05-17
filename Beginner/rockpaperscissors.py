import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
elif (computer_choice == 'rock' and user_choice == 'scissors') or \
     (computer_choice == 'paper' and user_choice == 'rock') or \
        (computer_choice == 'scissors' and user_choice == 'paper'):
    print("You lose!")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")  