import os
global font_size
font_size = input("Enter desired font size for the terminal (e.g., 12, 14, 16): ")
try:
    font_size_int = int(font_size)
    os.system(f'echo -e "\\033]50;SetFont=Monospace {font_size_int}\\007"')
    os.system("clear")
except ValueError:
    print("Invalid font size. Using default.")

import random

HINTS_FILE = "hints.txt"
authorisations_file = "authorisations_codes.txt"
words_file = "FiveLetterWords.csv"

def sync_hints_file():
    os.system('git add hints.txt && git commit -m "Auto-commit" && git push origin main')

if not os.path.exists(HINTS_FILE):
    with open(HINTS_FILE, "w") as f:
        f.write("0")
    sync_hints_file()

if not os.path.exists(authorisations_file):
    with open(authorisations_file, "w") as f:
        f.write("error")

if not os.path.exists(words_file):
    with open(words_file, "w") as f:
        print("error")

with open(authorisations_file, "r") as f:
    global codes
    codes = f.read().splitlines()
command = ""
code = ""
with open(HINTS_FILE) as f:
    hints = int(f.read())
user_guess = ""
win = False
word = ""
with open(words_file,"r") as f:
    content = f.read()
    words = content.split(",")
cWord = random.choice(words)
def evaluate_guess(user_guess, cWord):
    eval = ""
    for i in range(5):
        if user_guess[i] == cWord[i]:
            eval += user_guess[i]
        elif user_guess[i] in cWord:
            eval += "?"
        else:
            eval += "#"
    if user_guess != cWord:
        print("evaluation>> " + eval)
    

def validate(user_guess, wordlist):
    if user_guess == "commands":
        global command,font_size
        command = input("Enter a command: ")
        if command == "add hint" or command == "add hints":
            code = input("Enter the code: ")
            global add_hints
            add_hints = input("how many hints do you want to add? ")
            if code in codes:    
                with open(HINTS_FILE, "w") as f:    
                    f.write(add_hints)
                sync_hints_file()
                os.system("clear")
        if command == "minus hint" or command == "minus hints":
            code = input("Enter the code: ")
            global minus_hints
            minus_hints = input("how many hints do you want to remove? ")
            if code in codes:
                with open(HINTS_FILE, "w") as f:
                    f.write(str(int(hints) - int(minus_hints)))
                sync_hints_file()
                os.system("clear")
        if command == "reset hints" or command == "reset hint":
            code = input("Enter the code: ")
            if code in codes:
                with open(HINTS_FILE, "w") as f:
                    f.write("0")
                sync_hints_file()
                os.system("clear")
        if command == "set hints" or command == "set hint":
            code = input("Enter the code: ")
            global set_hints
            set_hints = input("how many hints do you want to set? ")
            if code in codes:
                with open(HINTS_FILE, "w") as f:
                    f.write(set_hints)
                sync_hints_file()
                os.system("clear")
        if command == "font size" or command == "fonts" or command == "font":
            code = input("Enter the code: ")
            font_size = input("Enter desired font size for the terminal (e.g., 12, 14, 16): ")
            if code in codes:
                try:
                    font_size_int = int(font_size)
                    os.system(f'echo -e "\\033]50;SetFont=Monospace {font_size_int}\\007"')
                    os.system("clear")
                except ValueError:
                    print("Invalid font size. Using default.")
    elif not user_guess.isalpha():
        print("enter a 5-letter word BEEP BEEP BOOP BOOP")
        return False
    elif len(user_guess) != 5:
        print("enter a five-letter word BEEP BEEP BOOP BOOP")
        return False
    elif user_guess not in wordlist:
        print("enter a real five-letter word BEEP BEEP BOOP BOOP")
        return False
    else:
        return True

def get_guess(wordlist):
    global hints
    global cWord
    global user_guess
    while True:
        user_guess = input("your guess>> ").lower()
        if user_guess == "restart":
            return "restart"
        elif user_guess == "help":
            print("enter a five-letter word, or type 'restart' to restart the game, or 'quit' to quit.")
        elif user_guess == "hint" and hints > 0:
            print("the word contains the letter: " + random.choice(cWord))
            hints -= 1
            with open(HINTS_FILE, "w") as f:
                f.write(str(hints))
            sync_hints_file()
            print("You have " + str(hints) + " hints left.")
        if validate(user_guess, wordlist):
            return user_guess
def play_game():
    global hints
    global cWord
    global win
    win = False
    cWord = random.choice(words)
while True:
    for i in range(7):
        if user_guess == "restart":
            cWord = random.choice(words)
            i = 0
            print("game restarted")
        print("guess " + str(i+1) + " of 6")
        user_guess = get_guess(words)
        evaluate_guess(user_guess, cWord)
        if user_guess == cWord:
                print("You win!")
                win = True
                hints += 1
                with open(HINTS_FILE, "w") as f:
                    f.write(str(hints))
                sync_hints_file()
                print("you have " + str(hints) + " hints now")
                break
        if win == False and i == 6:
            print("You lose! The word was: " + cWord)
    continue_game = input("Do you want to play again? (yes/no): ").lower()
    if continue_game == "yes":
        play_game()
    if  continue_game != "yes":
        print("PIGGY")
        play_game()
    user_guess = ""
    win = False
    hints = int(open(HINTS_FILE).read())
    cWord = random.choice(words)
    print("New game started. You have " + str(hints) + " hints.")
    print("you have " + str(hints) + " hints now")
    if win == False and i == 6:
        print("You lose! The word was: " + cWord)
    continue_game = input("Do you want to play again? (yes/no): ").lower()
    if continue_game == "yes":
        play_game()
    if  continue_game != "yes":
        print("PIGGY")
        play_game()
    user_guess = ""
    win = False
    hints = int(open(HINTS_FILE).read())
    cWord = random.choice(words)
    print("New game started. You have " + str(hints) + " hints.")