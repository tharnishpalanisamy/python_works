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

options = [rock,paper,scissors]
computer = random.randint(0,2)
valid_input=[0,1,2]
user = int(input("Enter 0 for rock , 1 for paper and 2 for scissor"))
print("Computer has choose ")
print(options[computer])
if user in valid_input:
    print("The user has choose")
    print(options[user])
    if user == 0 and computer == 2:
        print("you won !")
    if user == 2 and computer == 0:
        print("you lose !")
    elif user > computer:
        print("you won !")
    elif user < computer:
        print("You lose !")
    elif user == computer:
        print(" Draw ")
elif user not in valid_input:
    print("Invalid input")













