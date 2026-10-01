from random import choice

# import artk
logo = r"""
   _____ _      _   _   _                      _       
  / ____(_)    (_) | \ | |                    (_)      
 | |  __ _  ___ _  |  \| |_   _ _ __ ___  _ __ _ _ __  
 | | |_ | |/ _ \ | | . ` | | | | '_ ` _ \| '__| | '_ \ 
 | |__| | |  | | | |\  | |_| | | | | | | |  | | | | |
  \_____| |\___| | |_| \_|\__,_|_| |_| |_|_|  |_|_| |_|
       _/ |   _/ |                                     
      |__/   |__/                                      
"""

numbers_list = []
for nr in range(1,101):
    numbers_list.append(nr)

def guess_func(lives, ):
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: ")) #56
        if lives == 1 and guessed_number < think_number or lives == 1 and guessed_number > think_number:
            print("You've run out of guesses. Refresh the page to run again.")
            lives -= 1
        elif guessed_number < think_number:
            print("Too low. \nGuess again. ")
            lives -= 1
        elif guessed_number > think_number:
            print("Too high. \nGuess again. ")
            lives -= 1
        elif guessed_number == think_number:
            print(f"You got it. The number was {think_number}")
            lives = 0


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    think_number = choice(numbers_list)
    attempts = 10
    guess_func(attempts)

elif difficulty == 'hard':
    think_number = choice(numbers_list)
    attempts = 5
    guess_func(attempts)

else:
    pass
