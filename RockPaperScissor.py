import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock,Paper,Scissors, or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_chose = options[random_number]
    print("Computer chose", computer_chose + ".")

    if user_input == "rock" and computer_chose == "scissors":
        print("You won!")
        user_wins += 1
        

    elif user_input == "paper" and computer_chose == "rock":
        print("You won!")
        user_wins += 1
        
    
    elif user_input == "scissors" and computer_chose == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer wins", computer_wins, "times.")
print("Goodbye!")
