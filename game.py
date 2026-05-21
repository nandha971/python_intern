import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_images = [rock, paper, scissors]


while True:

    
    user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice! Please enter 0, 1, or 2.")
        continue

    
    computer_choice = random.randint(0, 2)

    
    print("\nYou chose:")
    print(game_images[user_choice])

    
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You Win!")

    else:
        print("You Lose!")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break