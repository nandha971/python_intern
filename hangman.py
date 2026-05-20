import random
words = ["johnny", "butcher", "luffy", "heisenberg", "zinta"]
word = random.choice(words)
hangman_stages = [
    """
----
|   |
    |
    |
    |
    |
=========
""",
    """
----
|   |
O   |
    |
    |
    |
=========
""",
    """
----
|   |
O   |
|   |
    |
    |
=========
""",
    """
----
|   |
O   |
/|  |
    |
    |
=========
""",
    """
----
|   |
O   |
/|\\ |
    |
    |
=========
""",
    """
----
|   |
O   |
/|\\ |
/    |
    |
=========
""",
    """
----
|   |
O   |
/|\\ |
/ \\ |
    |
=========
"""
]

hidden_word = ["_"] * len(word)
guessed_letters = []

wrong_attempts = 0
max_attempts = 6

print("WELCOME TO HANGMAN GAME")
print("Guess the word letter by letter!\n")


while wrong_attempts < max_attempts and "_" in hidden_word:

    print(hangman_stages[wrong_attempts])

    print("Word:", " ".join(hidden_word))

    guess = input("Enter a letter: ")

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue


    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    
    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")

        
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    
    else:
        wrong_attempts += 1
        print("Wrong guess! ")
        print("Attempts left:", 6 - wrong_attempts)


if "_" not in hidden_word:
    print("Congratulations! You guessed the word:", word)
else:
    print(hangman_stages[wrong_attempts])
    print("Game Over! The correct word was:", word)