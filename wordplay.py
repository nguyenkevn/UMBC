import colorama

# Loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in secret):
      
      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)
      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
        printColorfulLetter(letter, False, False)
    # Handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# Function that takes in a six-lettered word from the user
def getSixLetterInput():
  word = ""
  while (len(word) != 6):
    word = input("Enter a six letter word: ")
    word = word.upper()
  return word
# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

#Header and instructions

print(r"""
  _____                   _____         _____        _____              _____    ____               ____    _____      _____ 
 |\    \   _____     ____|\    \    ___|\    \   ___|\    \         ___|\    \  |    |         ____|\   \  |\    \    /    /|
 | |    | /    /|   /     /\    \  |    |\    \ |    |\    \       |    |\    \ |    |        /    /\    \ | \    \  /    / |
 \/     / |    ||  /     /  \    \ |    | |    ||    | |    |      |    | |    ||    |       |    |  |    ||  \____\/    /  /
 /     /_  \   \/ |     |    |    ||    |/____/ |    | |    |      |    |/____/||    |  ____ |    |__|    | \ |    /    /  / 
|     // \  \   \ |     |    |    ||    |\    \ |    | |    |      |    ||    |||    | |    ||    .--.    |  \|___/    /  /  
|    |/   \ |    ||\     \  /    /||    | |    ||    | |    |      |    ||____|/|    | |    ||    |  |    |      /    /  /   
|\ ___/\   \|   /|| \_____\/____/ ||____| |____||____|/____/|      |____|       |____|/____/||____|  |____|     /____/  /    
| |   | \______/ | \ |    ||    | /|    | |    ||    /    | |      |    |       |    |     |||    |  |    |    |`    | /     
 \|___|/\ |    | |  \|____||____|/ |____| |____||____|____|/       |____|       |____|_____|/|____|  |____|    |_____|/      
    \(   \|____|/      \(    )/      \(     )/    \(    )/           \(           \(    )/     \(      )/         )/         
     '      )/          '    '        '     '      '    '             '            '    '       '      '          '   
     """)

print(r"""
~~~~~~~~~Welcome to Word Play~~~~~~~~~

=====================================
-You have 5 tries to guess the word correctly.
-The word is SIX CHARACTERS long, and you must enter a guess of this length
-If a letter is in the correct place, it will be green
-If a letter is in the word but NOT in the correct place, it will be yellow
-If the letter is NOT in the word, it will be red
=====================================

""")

# Game Logic
secret = "HARBOR"
counter = 5
for i in range(5):
  guess = getSixLetterInput()
  printGuessAccuracy(guess, secret)
  counter -= 1
  if guess == secret:
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Congratulations, you are a Word Play master! You had {counter} turns left")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    exit()
  if i < 4: 
    print(f"\n\n{counter} turns left")
  else:
      print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print(f"Game Over. The word is {secret}")
  
    
  

