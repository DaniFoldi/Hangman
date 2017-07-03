# -*- coding: UTF-8 -*-

#SPECIAL THANKS:
#ÁDÁM FOR THE GAME IDEA AND LETTING ME OVERCOMPLICATE IT
#EASY AND MEDIUM WORDS FROM: https://www.thegamegal.com/printables/
#HARD WORDS FROM: https://www.hangmanwords.com/words
#COLORED TEXT: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

#IMPORT

from __future__ import print_function
import random
import csv
from decimal import *
import os
import platform
import sys

#WORD LIST

word_list = []

#VERSION

version = "v1.7"

#COLORED PRINTING (ONLY UNIX-BASED)

class color:
  pink = "\033[95m"
  blue = "\033[94m"
  green = "\033[92m"
  yellow = "\033[93m'"
  red = "\033[91m"
  bold = "\033[1m"
  underline = "\033[4m"
  end = "\033[0m"

#HANGMANIMATION

hangman_states = [
  ["",            "",           "",             "",            "",             "",   "_____________"],
  ["",            "",           "",             "",            "",             "",   "_⏊___________"],
  [" │",          " │",         " │",           " │",          " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │",         " │",           " │",          " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      😂️", " │",           " │",          " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      😄", " │       │",   " │       │",  " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      🙂", " │      /│",   " │       │",  " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      🙁", " │      /│\\", " │       │",  " │",           " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      😨", " │      /│\\", " │       │",  " │      /",    " │", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾⏋", " │      😱", " │      /│\\", " │       │",  " │      /\\",  " │", "_⏊___________"]
]

#MAXIMUM LIVES

lives_max = 10

#STATS

games_played = 0
games_won = 0
games_lost = 0

#DIFFICULTIES

difficulties = ["Easy", "Medium", "Hard"]

#ALPHABET

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#VARIABLES

selected_difficulty = ""
word = ""
characters_guessed = []
word_guessed = []
lives_left = 0

#FUNCTIONS

def print_right(text):
  rows, columns = os.popen('stty size', 'r').read().split()
  for i in range(0, int(columns) - len(text) + 13):
    print(" ", end = "")
  print(text)

def reset_word():
  global word_guessed
  word_guessed = []
  for i in range(0, len(word)):
    word_guessed.append("_")

def reset_game():
  global lives_left
  global word
  global characters_guessed
  lives_left = 10
  word = ""
  characters_guessed = []

def choose_word():
  global word
  if selected_difficulty in difficulties:
    word = word_list[random.randint(0, len(word_list) - 1)]
    reset_word()
  else:
    error("Incorrect difficulty selected")
    choose_difficulty()
    choose_word()

def error(text):
  print(color.red + text + color.end)

def header(text):
  print(color.pink + color.bold + text + color.end)

def move_cursor():
  nothing_yet = 2.0

def win():
  for char in word_guessed:
    if char == "_":
      return False
  return True
  
def guess_letter():
  global characters_guessed
  global lives_left
  global word_guessed
  print("Please input your guess")
  char = input("")
  char = char.lower()
  if char in alphabet:
    if char in characters_guessed:
      error("Letter already guessed")
      guess_letter()
    else:
      char_in_word = False
      for i in range(0, len(word)):
        if word[i] == char:
          word_guessed[i] = char
          char_in_word = True
      if not char_in_word:
        lives_left -= 1
      characters_guessed.append(char)
  else:
    error("Incorrect guess")
    guess_letter()
  
def print_lives():
  print("Lives: ", end = "")
  if lives_left < 10:
    print(" ", end = "")
  print(str(lives_left))

def print_stats():
  print_right("Difficulty: " + color.green + color.bold + selected_difficulty + color.end)
  print_right("Games played:    " + color.green + color.bold + str(games_played) + color.end)
  print_right("Games won:    " + color.green + color.bold + str(games_won) + color.end)
  print_right("Games lost:    " + color.green + color.bold +  str(games_lost) + color.end)
  if games_lost == 0:
    print_right("W/L Ratio:    " + color.green + color.bold + "-" + color.end)
  else:
    precision = getcontext().prec
    getcontext().prec = 2
    print_right("W/L Ratio:    " + color.green + color.bold + str(Decimal(games_won) / Decimal(games_lost))+ color.end)
    getcontext().prec = precision
  
def print_word():
  print(" ".join(word_guessed), end = "")
  print()

def print_guesses():
  for letter in alphabet:
    if letter in characters_guessed:
      print(color.green + letter + color.end, end = "")
    else:
      print(color.blue + letter + color.end, end = "")
    if letter != alphabet[len(alphabet) - 1]:
      print(" ", end = "")
  print()
  
def print_state():
  hangman_state()
  print_lives()
  print_word()
  print_guesses()
  
def lose():
  if lives_left <= 0:
    return True
  else:
    return False

def hangman_state():
  if lives_left < lives_max:
    for state in hangman_states[lives_max - 1 - lives_left]:
      print(state)
  
def choose_difficulty():
  global selected_difficulty
  print("Please select a difficulty level: " + color.green)
  print((color.end + " / " + color.green).join(difficulties), end = "")
  print(color.end)
  selected_difficulty = input("")
  selected_difficulty = selected_difficulty.capitalize()
  if selected_difficulty in difficulties:
    with open((selected_difficulty.lower() + ".csv"), newline = "") as word_file:
      reader = csv.reader(word_file, delimiter = " ", quotechar = "|")
      for option in reader:
        word_list.append(option[0])
  else:
    error("Difficulty not available")
    choose_difficulty()

  
#MAIN LOGIC
if __name__ == "__main__":
  if platform.system == "Windows":
    error("Windows is not supported right now")
    sys.exit(1)
  else:
    header("Welcome to the Ultimate Hangman " + version)
    choose_difficulty()
    while True:
      print()
      print()
      reset_game()
      choose_word()
      print_state()
      
      while not(win() or lose()):
        guess_letter()
        print_state()
        
      if win():
        print(color.bold + "You won the game! Congrats!" + color.end)
        games_won += 1
        games_played += 1
      elif lose():
        print(color.bold + "You lost." + color.end)
        print("The word was: " + color.red + word + color.end)
        games_lost += 1
        games_played += 1
      print()
      print_stats()