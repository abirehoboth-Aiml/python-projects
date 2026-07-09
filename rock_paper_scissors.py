import random

print("=== Rock Paper Scissors ===")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
elif user not in choices:
    print("Invalid choice!")
else:
    print("Computer wins!")
