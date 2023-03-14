import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_game()
