import random
to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
cards = [11,  10]
user_cards = []
computer_cards = []
def ace(cards):
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
def check_result(cards1,cards2):
    if sum(cards1) > 21 :
        print("you went over , You lose !")
    elif sum(cards2) > 21 :
        print("computer went over , you win !")
    elif 10 in cards1 and 11 in cards1 and len(cards1) == 2:
        print("BlackJack , you win !")
    elif 10 in cards2 and 11 in cards2 and len(cards2) == 2:
        print("BlackJack for computer , you lose !")
    elif sum(cards1) > sum(cards2) and sum(cards1) <= 21 :
        print("You win !")
    elif sum(cards2) > sum(cards1) and sum(cards2) <= 21 :
        print("You lose !")
    elif sum(cards1) == sum(cards2) :
        print("Draw")
if to_play == "y":
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    ace(user_cards)
    ace(computer_cards)
    print(f"User cards : {user_cards} score :{sum(user_cards)}")
    print(f"computers first card {computer_cards[0]}")
    if sum(user_cards) == 21 and len(user_cards) == 2:
        print("BlackJack! You win!")
    elif sum(computer_cards) == 21 and len(computer_cards) == 2:
        print("BlackJack for computer! You lose!")
    else:
        game_over = False
        while not game_over:
            to_continue = input("Type 'y' to get another card, type 'n' to pass:")
            if to_continue == "y" :
                user_cards.append(random.choice(cards))
                ace(user_cards)
                print(f"your cards :{user_cards}  your score : {sum(user_cards)}")
                if sum(user_cards) > 21 :
                    print("you went over ! game over !")
                    game_over = True
            elif to_continue == "n" :
                while sum(computer_cards) < 17 :
                    computer_cards.append(random.choice(cards))
                    ace(computer_cards)
                print(f"Computers card:{computer_cards}  computer score:{sum(computer_cards)}")
                check_result(user_cards,computer_cards)
                game_over = True
            else:
                print("Enter a valid input !")
else:
    print("Okay have a nice day !")
