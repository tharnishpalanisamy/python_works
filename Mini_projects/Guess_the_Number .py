import random
import art
print(art.logo)
print("Welcome to number guessing game ")
print("Iam thinking a number between 1 and 100 ")
correct_number = random.randint(1,100)
# print(correct_number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
def game(difficulty,answer):
    lives = 0
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Invalid input :( ")
    game_over = False
    while not game_over:
        print(f"You have {lives} lives remaining ")
        guess = int(input("Make a guess :"))
        if guess > answer:
            print("Too high")
            lives -= 1
        elif guess < answer:
            print("Too low")
            lives -= 1
        elif guess == answer:
            print(f"You guess {guess} which is the Right Answer :) !")
            game_over = True
        if lives == 0 :
            game_over = True
            print("You lost all your lives ")
            print(f"The right answer was {answer}")
game(difficulty,correct_number)



