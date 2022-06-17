"""
Name(s): Austin Wai
Name of Project: Hangman Project

I didn't realize that I had to click on the class github link until today, 6/14, so I will be copying and pasting my code from my other replit project I was working on.

"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
# By Austin Wai
# Project: Hangman

from page1 import words
import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def selectRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]
#Selects a random word from my word list.

def screen(missedLetters, correctLetters, mysteryWord):
  print(HANGMAN_PICS[len(missedLetters)])
  print()

  print('Missed letters:', end=' ')
  for letter in missedLetters:
    print(letter, end=' ')
  print()

  blanks = '_' * len(mysteryWord)

  for i in range(len(mysteryWord)):
    if mysteryWord[i] in correctLetters:
      blanks = blanks[:i] + mysteryWord[i] +       blanks[i+1:]
  for letter in blanks:
    print(letter, end=' ')
  print()
#Controls visual display (Hangman image, blanks, letters, etc.)

def Guess(alreadyGuessed):
  while True:
    print('Guess a letter.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in alreadyGuessed:
      print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
       print('Please enter a LETTER.')
    else:
       return guess
#Returns the letter that the player entered. Also ensures that the player enters letters only, and only one letter at a time.
      
def playAgain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')
#If the player wants to play again, this function returns True; if the player does not want to play again, it returns False.

print('Welcome to Hangman. You will have 6 chances to guess the mystery word, one at a time. You may only enter letters; numbers and special characters are not allowed. Good luck!')
missedLetters = ''
correctLetters = ''
mysteryWord = selectRandomWord(words)
gameIsDone = False

while True:
  screen(missedLetters, correctLetters, mysteryWord)
#Allows the player to enter a letter.
  
  guess = Guess(missedLetters + correctLetters)
  if guess in mysteryWord:
    correctLetters = correctLetters + guess
#Checks if the player won the game.
    
    foundAllLetters = True
    for i in range(len(mysteryWord)):
      if mysteryWord[i] not in correctLetters:
        foundAllLetters = False
        break
    if foundAllLetters:
      print('Congratulations! You won the game! Your word was ' + mysteryWord)
      gameIsDone = True
  else:
    missedLetters = missedLetters + guess
#Checks if the player lost.

    if len(missedLetters) == len(HANGMAN_PICS) - 1:
      screen(missedLetters, correctLetters, mysteryWord)
      print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + mysteryWord + '"')
      gameIsDone = True
#Asks the player if they want to play again once the game is finished.
      
  if gameIsDone:
    if playAgain():
      missedLetters = ''
      correctLetters = ''
      gameIsDone = False
      mysteryWord = selectRandomWord(words)
    else:
      break
  