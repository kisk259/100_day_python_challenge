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

# Write your code below this line 👇
choices = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0, 3)
player = choices[player_input]
computer = choices[computer_input]

print(player)
print("Computer chose:")
print(computer)

if player == rock and computer == scissors:
    print("You Win")
elif player == scissors and computer == paper:
    print("You Win")
elif player == paper and computer == rock:
    print("You Win")
elif player == computer:
    print("Draw")
else:
    print("You Lose")
