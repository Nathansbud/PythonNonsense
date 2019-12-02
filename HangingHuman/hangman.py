#!/usr/local/bin/python3.7

from sys import argv
import random
import trash

win = 0
loss = 0
max_lives = 6

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def play(word=None):
    global win
    global loss
    global max_lives
    global w
    w = None

    if word:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        word_path = "/usr/share/dict/web2"
        word = random.choice(open(word_path).readlines()).strip().lower()
    print("Welcome to Hangman! Your word has been chosen...")

    guess = " " * len(word)
    display = ""
    guessed = []
    lives = max_lives

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
    w = None
    if argv[1:]:
        args = [arg.lower() for arg in argv[1:]]
        if '-l' in args:
            try:
                max_lives = int(args[args.index('-l')+1])
            except IndexError:
                print("Argument -l must be followed by a number!")
            except ValueError:
                print("Argument -l must be followed by a number!")
        if '-w' in args:
            try:
                w = args[args.index('-w')+1]
            except IndexError:
                print("Argument -w must be followed by a word!")
            if w and not str.isalpha(w):
                w = None
                print("Word must be alphabetic!")
    playing = True
    while playing:
        try:
            playing = play(w)
        except KeyboardInterrupt:
            print()
            exit(0)


