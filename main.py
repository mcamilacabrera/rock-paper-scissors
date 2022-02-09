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

#Write your code below this line 👇

human_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
human_choice = int()

import random

computer_choice = random.randint(0, 2)
print(computer_choice)
print(type(human_choice))
print(type(computer_choice))

if human_choice == 0:
    print(rock)
elif human_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if human_choice == 0 & computer_choice == 1:
    print("computer wins!!")
elif human_choice == 0 & computer_choice == 2:
    print("you win!!")
elif human_choice == 0 & computer_choice == 0:
    print("DRAW")
elif human_choice == 1 & computer_choice == 0:
    print("you win!!")
elif human_choice == 1 & computer_choice == 2:
    print("computer wins!!")
elif human_choice == 1 & computer_choice == 1:
    print("DRAW")
elif human_choice == 2 & computer_choice == 0:
    print("computer wins!!")
elif human_choice == 2 & computer_choice == 1:
    print("you win!!")
elif human_choice == 2 & computer_choice == 2:
    print("DRAW")
else:
    print("ff")
