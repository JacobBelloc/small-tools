import random

print("Let's play rock, paper, scissors!")
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(['rock', 'paper', 'scissors'])

print(f"Your choice: {player_choice}")
print(f"Computer's choice: {computer_choice}")

if player_choice == computer_choice:
    print("Tie!")
elif (player_choice == 'rock' and computer_choice == 'scissors') or \
     (player_choice == 'paper' and computer_choice == 'rock') or \
     (player_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")
