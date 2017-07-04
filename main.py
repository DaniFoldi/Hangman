# -*- coding: UTF-8 -*-

#SPECIAL THANKS:
#ÁDÁM FOR THE GAME IDEA AND LETTING ME OVERCOMPLICATE IT
#IMPOSSIBLE WORDS FROM: https://www.hangmanwords.com/words
#COLORED TEXT: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

#PLANS FOR THE FUTURE:
#LANG SUPPORT
#GLOBAL LEADERBOARD
#iOS RELEASE

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

#CONSTANTS

version = "v2.0ß"
lives_max = 10
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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

#STATS

games_played = 0
games_won = 0
games_lost = 0
total_guesses = 0

#CATEGORIES

categories = ["Animals", "Cars", "City", "Colors", "Countries", "Family", "House", "Impossible", "Meals", "Movies", "Music", "School", "Tech"]

#VARIABLES

selected_category = ""
word = ""
characters_guessed = []
word_guessed = []
lives_left = 0

#FUNCTIONS

def print_right(text, length):
  if length <= 0:
    length = len(text)
  rows, columns = os.popen('stty size', 'r').read().split()
  for i in range(int(columns) - length):
    print(" ", end = "")
  print(text)

def error(text):
  print(color.red + text + color.end)

def header(text):
  print(color.pink + color.bold + text + color.end)

def highlight(text):
  print(color.bold + text + color.end)

def reset_word(word):
  word_guessed = []
  for i in range(len(word)):
    word_guessed.append("_")
  return word_guessed

def reset_game():
  global lives_left
  global word
  global characters_guessed
  lives_left = lives_max
  word = ""
  characters_guessed = []

def choose_category(categories):
  global selected_category
  global word_list
  print("Please select a category: " + color.green)
  print((color.end + " / " + color.green).join(categories), end = "")
  print(color.end)
  selected_category = input("").capitalize()
  if selected_category in categories:
    word_list = load_words(selected_category)
  else:
    error("Category not available")
    choose_category(categories)

def choose_word(word_list):
  word = word_list[random.randint(0, len(word_list) - 1)]
  word_guessed = reset_word(word)
  return word, word_guessed

def load_words(selected_category):
  word_list = []
  with open((selected_category.lower() + ".csv"), newline = "") as word_file:
      reader = csv.reader(word_file, delimiter = " ", quotechar = "|")
      for option in reader:
        word_list.append(option[0])
  return word_list
  
def guess_letter():
  global characters_guessed
  global lives_left
  global word_guessed
  global total_guesses
  print("Please input your guess")
  char = input("")
  char = char.lower()
  if char in alphabet:
    if char in characters_guessed:
      error("Letter already guessed")
      guess_letter()
    else:
      char_in_word = False
      for i in range(len(word)):
        if word[i] == char:
          word_guessed[i] = char
          char_in_word = True
      if not char_in_word:
        lives_left -= 1
      characters_guessed.append(char)
  else:
    error("Incorrect guess")
    guess_letter()
  
def print_lives(lives_left):
  print("Lives: ", end = "")
  if lives_left < 10:
    print(" ", end = "")
  highlight(str(lives_left))

def print_stats(stats):
  max_length = 0
  for stat in stats:
    if len(stat[1]) > max_length:
      max_length = len(stat[1])
  for stat in stats:
    display = stat[0]
    for i in range(max_length - len(stat[1])):
      display += " "
    length = len(stat[0]) + max_length
    display += color.green + color.bold + stat[1] + color.end
    print_right(display, length)
  
def print_word(word_guessed):
  print(" ".join(word_guessed), end = "")
  print()

def print_guesses():
  for letter in alphabet:
    if letter in characters_guessed:
      print(color.green + letter + color.end, end = "")
    else:
      print(color.blue + color.bold + letter + color.end, end = "")
    if letter != alphabet[-1]:
      print(" ", end = "")
  print()
  
def print_state(lives_left, lives_max, word_guessed):
  hangman_state(lives_left, lives_max)
  print_lives(lives_left)
  print_word(word_guessed)
  print_guesses()

def stats(selected_category, games_played, games_won, games_lost, total_guesses):
  stats = [["Category: ", selected_category], ["Games played: ", str(games_played)], ["Games won: ", str(games_won)], ["Games lost: ", str(games_lost)], ["W/L Ratio: "], ["Average guesses: "]]
  if games_lost == 0:
    stats[4].append("-")
  else:
    precision = getcontext().prec
    getcontext().prec = 2
    stats[4].append(str(Decimal(games_won) / Decimal(games_lost)))
    getcontext().prec = precision

  if games_played == 0:
    stats[5].append("-")
  else:
    precision = getcontext().prec
    getcontext().prec = 2
    stats[5].append(str(Decimal(total_guesses) / Decimal(games_played)))
    getcontext().prec = precision
  print_stats(stats)

def win(word_guessed):
  for char in word_guessed:
    if char == "_":
      return False
  return True
  
def lose(lives_left):
  if lives_left <= 0:
    return True
  else:
    return False

def hangman_state(lives_left, lives_max):
  if lives_left < lives_max:
    for state in hangman_states[lives_max - 1 - lives_left]:
      print(state)

def move_cursor():
  nothing_yet = 2.0

#MAIN LOGIC
if __name__ == "__main__":
  if platform.system == "Windows":
    error("Windows is not supported right now")
    sys.exit(1)
  else:
    header("Welcome to the Ultimate Hangman " + version)
    if len(sys.argv) > 1:
      if sys.argv[1] == "easy":
        word_list = load_words("easy")
        selected_category = "easy"
      elif sys.argv[1] == "medium":
        word_list = load_words("medium")
        selected_category = "medium"
      elif sys.argv[1] == "hard":
        word_list = load_words("impossible")
        selected_category = "hard"
      elif sys.argv[1] == "debug":
        word_list = ["computer"]
        selected_category = "Debug"
      else:
        choose_category(categories)
    else:
      choose_category(categories)
    while True:
      print()
      reset_game()
      word, word_guessed = choose_word(word_list)
      print_state(lives_left, lives_max, word_guessed)

      while not(win(word_guessed) or lose(lives_left)):
        guess_letter()
        print_state(lives_left, lives_max, word_guessed)
        
      if win(word_guessed):
        highlight(color.bold + "You won the game! Congrats!" + color.end)
        games_won += 1
        games_played += 1
        total_guesses += len(characters_guessed)
      elif lose(lives_left):
        highlight(color.bold + "You lost." + color.end)
        print("The word was: " + color.red + word + color.end)
        games_lost += 1
        games_played += 1
      print()

      stats(selected_category, games_played, games_won, games_lost, total_guesses)