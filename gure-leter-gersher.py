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
import random
import sys

#First Step - User Choice
user_choice = int(input("Cfare zgjedh? Shkruaj 0 per Gure, 1 per Leter dhe 2 per Gershere\n"))
game_images = [rock, paper, scissors]

if user_choice not in [0,1,2]:
    print("Duhet te perdoresh numrat 0-1-2. Provoje perseri")
    sys.exit()
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer choose:\n" + game_images[computer_choice])

if user_choice == computer_choice:
    print("Barazim")
elif user_choice == 0 and computer_choice == 2:
    print("Fitove")
elif user_choice == 2 and computer_choice == 0:
    print("Humbe")
elif user_choice < computer_choice:
    print("Humbe")
elif user_choice > computer_choice:
    print("Fitove")