import random
import art
import game_data

def game():
    score = 0
    a = random.choice(game_data.data)
    game_over = False
    while not game_over:
        b = random.choice(game_data.data)
        while a == b:
            b = random.choice(game_data.data)
        print(art.logo)
        print(f"Compare A : {a["name"]} , a {a["description"]}, from {a["country"]}")
        print(art.vs)
        print(f"against B : {b["name"]} , a {b["description"]}, from {b["country"]}")
        choice = input("Who has more followers? Type 'A' or 'B':").lower()
        if choice == "a" and a["follower_count"]  >  b["follower_count"] :
            score += 1
            print(f"You're right! current score:{score}")
            a = b
        elif choice == "b" and a["follower_count"]  <  b["follower_count"] :
            score += 1
            print(f"You're right! current score:{score}")
            a = b
        else :
            print(f"Sorry, that's wrong. Final score:{score}")
            game_over = True


game()





















