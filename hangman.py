import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew", "kiwi", "lemon"]

word = random.choice(words)
letters = set(word)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
used_letters = set()

while len(letters) > 0:
    print("Current word: ", end="")
    for letter in word:
        if letter in used_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()

    user_letter = input("Guess a letter: ").lower()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in letters:
            letters.remove(user_letter)
        else:
            print("Letter is not in word.")
    elif user_letter in used_letters:
        print("You already used that letter. Guess another one.")
    else:
        print("Invalid character. Please try again.")

print(f"Congratulations! The word was {word}. You win!")
