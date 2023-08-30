import random
from art import logo

pc_random = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
def game():
    # Tahmin döngüsü şartı:
    end_game = True
    stage = input("Choose a difficulty: Type 'hard' or 'easy': ")
    if stage.lower() == "hard":
        health = 5
    elif stage.lower() == "easy":
        health = 10
    # Tahmin döngüsü:
    while end_game:
        user_guess = int(input("Make a guess: "))
        if user_guess == pc_random:
            print(f"You win. Number is : {pc_random}")
            end_game = False
        elif user_guess > pc_random:
            # Son tahminde tekrar tahmin et ve bu kadar canın kaldı dememesi için koşul:
            if health - 1 > 0:
                print(f"Too high.\nGuess again.\nYou have {health - 1} attempts remaining to guess the number.")
            else:
                print("Too high.")
        elif user_guess < pc_random:
            if health - 1 > 0:
                print(f"Too low.\nGuess again.\nYou have {health - 1} attempts remaining to guess the number.")
            else:
                print("Too low.")
        health -= 1
        # Can bittiğinde oyunu sonlandıran koşul:
        if health == 0:
            print("Your health is not exist.")
            end_game = False
game()


# ******************************************

# Second way

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# def check_answer(guess, answer, turns):
#     """Checks answer against guess. Returns the number of turns remaining."""
#     if guess > answer:
#         print("Too high.")
#         return turns - 1
#     elif guess < answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}")

# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
    
# def game():
#     print(logo)
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100")
#     answer = random.randint(1,100)
#     print(f"Hey, the correct answer is {answer}")

#     turns = set_difficulty()

#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")

#         guess = int(input("Make a guess: "))

#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
# game()