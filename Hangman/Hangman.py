import random
import hangman_words
from hangman_art import logo
from hangman_art import stages
print(logo)

chosen_word = random.choice(hangman_words.word_list)
#print(f'Pssst, the solution is {chosen_word}.')

display = ["_"] * len(chosen_word)
print("Your word is: ")
print(" ".join(display))
print("                 ")
lives = 6

while "_" in display and lives > 0:
    guess = input("Guess a letter: \n").lower()
    print("                 ")
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(" ".join(display))
    else:
        lives -= 1
        print(stages[lives])
        print(" ".join(display))

if "_" not in display:
    print("Congratulations! You Win!")
else:
    print("Game Over! You Lose :(")
    print("The words was " + chosen_word)
