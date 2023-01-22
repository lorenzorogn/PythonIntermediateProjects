import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# press = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for \
# Scissors.")

# lista = [rock, paper, scissors]

# lista_random = random.choice(lista)

# if press == 0:
#     print(rock)
#     print("Computer chose:")
#     print(lista_random)
#     if lista_random == rock:
#         print("It's a draw")
#     elif lista_random == paper:
#         print("You lose")
#     else:
#         print("You win")
# elif press == 1:
#     print(paper)
#     print("Computer chose:")
#     print(lista_random)
#     if lista_random == rock:
#         print("You lose")
#     elif lista_random == paper:
#         print("It's a draw")
#     else:
#         print("You lose")
# else:
#     print(scissors)
#     print("Computer chose:")
#     print(lista_random)
#     if lista_random == rock:
#         print("You lose")
#     elif lista_random == paper:
#         print("You win")
#     else:
#         print("It's a draw")


# lei lo fa in maniera molto più semplice 

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for \
Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")




