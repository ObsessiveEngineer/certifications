################ Project: Hangman ################
import random
import words
from hangman_art import hangman_stages

lives = 6
def lose():
    render()
    print("YOU LOSE!")
    quit()

def win():
    render()
    print("YOU WIN!")
    quit()

def render():
    print(f"********************************{lives}/6 Lifes Left********************************")
    print(hangman_stages[hangman_index])


print("Welcome to the Hangman!")
chosen_word = random.choice(words.words)
guessed = ["_" for i in chosen_word]
hangman_index = 0
while True:
    render()
    print(f"Word to guess:  {" ".join(guessed)}")
    guessed_letter = input("Guess a letter: ").lower()
    if not (guessed_letter in chosen_word):
        lives -= 1 
        hangman_index += 1
        if (lives == 0):
            lose()

    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guessed_letter:
                guessed[i] = guessed_letter
        if chosen_word == "".join(guessed):
            win()