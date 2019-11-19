#!/usr/local/bin/python3.7
import platform
import random

win = 0
loss = 0

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def play():
    global win
    global loss

    print("Welcome to Hangman! Your word has been randomly generated...")
    word_path = "/usr/share/dict/web2"
    word = random.choice(open(word_path).readlines()).strip()
    guess = " " * len(word)
    display = ""
    guessed = []
    lives = 6

    while not guess == word and lives > 0:
        for c in guess:
            if c == " ": display += "_ "
            else: display += c + " "
        print(f"Current Guess: {display.rstrip()} | Lives: {lives} | W-L: {win}-{loss} | Guessed: {', '.join(guessed)}" )
        letter = input("Please input a letter: ").lower().strip()
        if letter == 'quit':
            exit(0)
        elif len(letter) != 1 or not letter.isalpha():
            print("Input must be a letter!")
        elif letter in guessed:
            print("You've already guessed that letter!")
        elif letter in word and not letter in guess:
            guess_letters = list(guess)
            for index in find(word, letter):
                guess_letters[index] = letter
            guess = ''.join(guess_letters)
            guessed.append(letter)
        elif letter not in word:
            print("Incorrect letter! Losing a life...")
            lives -= 1
            guessed.append(letter)
        else: print("UWU")
        display = ""
    if lives > 0:
        win += 1
    else:
        loss += 1
    print(f"You {'win' if lives > 0 else 'lose'}! The word was '{word}'!")
    replay_options = ['yes', 'y']
    quit_options = ['no', 'n', 'quit']
    choice = ""
    while not choice in replay_options + quit_options:
        choice = input("Play again (Y/N)? ").lower().strip()

    if choice in replay_options:
        return True
    return False



if __name__ == '__main__':
    playing = True
    while playing:
        playing = play()



