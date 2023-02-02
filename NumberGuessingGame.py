from Art import logo_nuber_guessing_game
import random
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
end_of_game = False
turns = 0

def check_answer(guess, answer, turns):
    clear()
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

    print(logo_nuber_guessing_game)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ")) 

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose. ")
            return
        elif guess != answer:
            print("Guess again.")

game()

restart = input(print("This repl has exited, run again?: 'yes' or 'no' "))

if restart == "no":
    end_of_game = True

while not end_of_game:
    clear()
    game()




# def game():
        
#     def number_checked(selected_number):
#         clear()
#         if selected_number == number:
#             print(f"You got it! The answer was {selected_number}")
#         elif selected_number > number:
#             print("Too high.")
#             print("Guess again.")        
#         else:
#             print("Too low.")
#             print("Guess again.")
        
#     print(logo_nuber_guessing_game)
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#     end_of_game = False

#     number = random.randrange(1, 101)

#     attempts = 0

#     if difficulty == "hard":
#         attempts = 5
#     else:
#         attempts = 10

#     while not end_of_game:

#         print(f"You have {attempts} attempts remaining to guess the number.")
#         number_guessed = int(input("Make a guess: "))
#         if number_guessed == number:
#             end_of_game == True
#         number_checked(number_guessed)
#         attempts -= 1
#         if attempts == 0:
#             print("You've run out of guesses, you lose.") 
#             end_of_game = True
#     else:
#         restart = input(print("This repl has exited, run again?: 'yes' or 'no' \n"))
#         if restart == "yes":
#             clear()
#             game()

# game()