rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game=[rock,paper,scissor]

import random
user=int(input('Enter number:0 for Rock,1 for Paper,2 for Scissors:'))
if user>=3 or user<0:
    print('You entered invalid number and you lose')
else:
    print(game[user])
    computer=random.randint(0,2)
    print('Computer choise:')
    print(game[computer])
    if user==computer:
        print("It's draw")
    elif computer==0 and user==2:
        print('You lose')
    elif user==0 and computer==2:
        print("You win")
    elif user<computer:
        print('You lose')
    elif user>computer:
        print("You win")
