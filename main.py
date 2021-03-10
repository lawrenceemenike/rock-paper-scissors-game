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
game_options = [rock, paper, scissors]


num_selected = int(input('what do you choose? type 0 for Rock, 1 for Paper or 2 for scissors\n'))
print('\n')
print('My Selection')
print(game_options[num_selected])
print('\n')

computer_selection = random.randint(0, 2)
print("Computer's Selection")
print(game_options[computer_selection])


if num_selected >= 3 or num_selected < 0:
  print('You typed an invalid number ')
elif  num_selected == 0 and computer_selection == 2:
  print('You win')
elif computer_selection == 0 and num_selected == 2:
  print('You lose')
elif computer_selection > num_selected:
  print('You lose')
elif num_selected > computer_selection:
  print('You Win')
elif num_selected == computer_selection:
  print('Its a draw')
