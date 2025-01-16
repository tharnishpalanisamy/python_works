import random
import hangman_words
import hangman_art
print(hangman_art.logo)
word_list = hangman_words.word_list
stages = hangman_art.stages
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"**************************** {lives} LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters :
        print(f"you have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} which is not in the word , you lost a life :( ")
        print(f"You have {lives} lives left")
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives])
