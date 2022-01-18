NUMBER GUESSING GAME PROJECT


import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5
    
else:
    attempts = 10


answer = random.randint(1,20)  #randint includes both 1 and 100

is_game_over = False

while is_game_over == False:
    
        
    print(f"\nYou have {attempts} attempts remaining to guess the answer")
    guess = int(input("Make a guess: "))
    
    if guess > answer:
        print("Too high.")
        attempts = attempts - 1

    elif guess < answer:
        print("Too low.")
        attempts = attempts - 1
        
    else:
        print(f"You got it! The answer is {answer}")
        is_game_over = True
        
    
    if attempts == 0:
        is_game_over = True
        print("\nYou've run out of guesses. You lose")
        print(f"\nThe answer is {answer}")
    if is_game_over == False:
        print("Guess again")