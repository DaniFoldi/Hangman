# -*- coding: UTF-8 -*-

#SPECIAL THANKS:
#ÁDÁM FOR THE GAME IDEA AND LETTING ME OVERCOMPLICATE IT
#IMPOSSIBLE WORDS FROM: https://www.hangmanwords.com/words

#PLANS FOR THE FUTURE:
#LANG SUPPORT
#GLOBAL LEADERBOARD
#CUSTOM WORDLIST
#iOS RELEASE

#IMPORT

from __future__ import print_function
import random
import csv
from decimal import *
import os
import platform
import sys

#CONSTANTS

version = "v2.4"
lives_max = 10
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
categories = ["Animals", "Atoms", "Cars", "City", "Colors", "Countries", "Family", "House", "Impossible", "Meals", "Movies", "Music", "Random", "School", "Tech"]

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

#COLORED PRINTING (ONLY UNIX-BASED)

class style:
  red = "\033[91m"
  pink = "\033[95m"
  yellow = "\033[93m"
  green = "\033[92m"
  blue = "\033[94m"
  bold = "\033[1m"
  underline = "\033[4m"
  end = "\033[0m"

#STATS

games_played = 0
games_won = 0
games_lost = 0
total_guesses = 0

#VARIABLES

selected_category = ""
word = ""
characters_guessed = []
word_guessed = []
lives_left = 0
word_list = []
random_mode = False

#FUNCTIONS

def get_text(text):
  if sys.version_info[0] > (2):
    return input(text)
  else:
    return raw_input(text)

def get_terminal_size():
  width, height = os.popen('stty size', 'r').read().split()
  return width, height

def clear_terminal():
  width, height = get_terminal_size()
  for i in range(int(width)):
    print()

def print_right(text, length):
  if length <= 0:
    length = len(text)
  width, height = get_terminal_size()
  for i in range(int(height) - length):
    print(" ", end = "")
  print(text)

def error(text):
  print(style.red + text + style.end)

def header(text):
  print(style.pink + style.bold + text + style.end)

def highlight(text):
  print(style.bold + text + style.end)

def print_inline(text):
  print(text, end = "")

def reset_word(word):
  word_guessed = []
  for i in range(len(word)):
    if word[i] == " ":
      word_guessed.append(" ")
    elif word[i] == "-":
      word_guessed.append("-")
    else:
      word_guessed.append("_")
  return word_guessed

def reset_game(lives_max):
  lives_left = lives_max
  word = ""
  characters_guessed = []
  return lives_left, word, characters_guessed

def choose_category(categories):
  print("Please select a category: " + style.green)
  for category in categories:
    if category == "Impossible":
      print_inline(style.red + style.bold + category + style.end)
    elif category == "Random":
      print_inline(style.green + style.bold + category + style.end)
    else:
      print_inline(style.blue + category + style.end)
    if category != categories[-1]:
      print_inline(" / ")
  print()
  selected_category = get_text("").capitalize()
  if selected_category not in categories:
    error("Category not available")
    selected_category = choose_category(categories)
  return selected_category

def choose_word(word_list):
  word = random.choice(word_list).upper()
  word_guessed = reset_word(word)
  return word, word_guessed

def choose_word_list(categories):
  if len(sys.argv) > 1:
    if sys.argv[1] == "easy":
      selected_category = "easy"
      word_list = load_words("easy")
      return word_list, selected_category, False
    elif sys.argv[1] == "medium":
      selected_category = "medium"
      word_list = load_words("medium")
      return word_list, selected_category, False
    elif sys.argv[1] == "hard":
      selected_category = "hard"
      word_list = load_words("impossible")
      return word_list, selected_category, False
    elif sys.argv[1] == "debug":
      selected_category = "Debug"
      word_list = ["TEST word - ALL specials"]
      return word_list, selected_category, False
    
  selected_category = choose_category(categories)
  random_mode = False
  word_list = []
  if selected_category == "Random":
    random_mode = True
  else:
    word_list = load_words(selected_category)
  return word_list, selected_category, random_mode

def load_words(selected_category):
  word_list = []
  with open((selected_category.lower() + ".csv")) as word_file:
      reader = csv.reader(word_file, delimiter = ",", quotechar = "|")
      for option in reader:
        word_list.append(option[0])
  return word_list
  
def guess_letter(alphabet, characters_guessed, word, word_guessed, lives_left):
  print("Please input your guess")
  char = get_text("")
  char = char.upper()
  if char in alphabet:
    if char in characters_guessed:
      error("Letter already guessed")
      lives_left, word_guessed, characters_guessed = guess_letter(alphabet, characters_guessed, word, word_guessed, lives_left)
      return lives_left, word_guessed, characters_guessed
    else:
      char_in_word = False
      for i in range(len(word)):
        if word[i] == char:
          word_guessed[i] = char
          char_in_word = True
      if not char_in_word:
        lives_left -= 1
      characters_guessed.append(char.upper())
      return lives_left, word_guessed, characters_guessed
  else:
    error("Incorrect guess")
    lives_left, word_guessed, characters_guessed = guess_letter(alphabet, characters_guessed, word, word_guessed, lives_left)
    return lives_left, word_guessed, characters_guessed
  
def print_lives(lives_left):
  print_inline("Lives: ")
  if lives_left < 10:
    print_inline(" ")
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
    display += style.green + style.bold + stat[1] + style.end
    print_right(display, length)
  
def print_word(word_guessed):
  print_inline(" ".join(word_guessed))
  print()

def print_guesses(alphabet, characters_guessed):
  for letter in alphabet:
    if letter in characters_guessed:
      if letter in word:
        print_inline(style.green + letter.upper() + style.end)
      else:
        print_inline(style.red + letter.upper() + style.end)
    else:
      print_inline(style.blue + style.bold + letter.upper() + style.end)
    if letter != alphabet[-1]:
      print_inline(" ")
  print()
  
def print_state(lives_left, lives_max, word_guessed, alphabet, characters_guessed):
  hangman_state(lives_left, lives_max)
  print_lives(lives_left)
  print_word(word_guessed)
  print_guesses(alphabet, characters_guessed)

def stats(selected_category, games_played, games_won, games_lost, total_guesses):
  stats = [["Category: ", selected_category], ["Games played: ", str(games_played)], ["Games won: ", str(games_won)], ["Games lost: ", str(games_lost)], ["W/L Ratio: "], ["Average guesses: "]]
  if games_lost == 0:
    stats[4].append("-")
  else:
    stats[4].append(str(ratio(games_won, games_lost)))
  if games_played == 0:
    stats[5].append("-")
  else:
    stats[5].append(str(ratio(total_guesses, games_played)))
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

def ratio(dividend, divisor):
  precision = getcontext().prec
  getcontext().prec = 2
  result = Decimal(dividend) / Decimal(divisor)
  getcontext().prec = precision
  return result

def move_cursor():
  nothing_yet = 3.0

#MAIN LOGIC
if __name__ == "__main__":
  clear_terminal()

  broadened_category_list = categories[:]
  broadened_category_list.remove("Random")
  broadened_category_list.remove("Impossible")

  if platform.system == "Windows":
    error("Windows is not supported right now")
    sys.exit(1)
  else:
    header("Welcome to the Ultimate Hangman {}".format(version))
    word_list, selected_category, random_mode = choose_word_list(categories)
    while True:
      print()
      lives_left, word, characters_guessed = reset_game(lives_max)

      if random_mode == True:
        selected_category = random.choice(broadened_category_list)
        word_list = load_words(selected_category)
        print_inline("Category: ")
        highlight(selected_category)

      word, word_guessed = choose_word(word_list)

      while not(win(word_guessed) or lose(lives_left)):
        print_state(lives_left, lives_max, word_guessed, alphabet, characters_guessed)
        lives_left, word_guessed, characters_guessed = guess_letter(alphabet, characters_guessed, word, word_guessed, lives_left)
      
      print_state(lives_left, lives_max, word_guessed, alphabet, characters_guessed)

      if win(word_guessed):
        highlight(style.bold + "You won the game! Congrats!" + style.end)
        games_won += 1
        games_played += 1
        total_guesses += len(characters_guessed)
      elif lose(lives_left):
        highlight(style.bold + "You lost." + style.end)
        print("The word was: " + style.red + word + style.end)
        games_lost += 1
        games_played += 1
      print()

      stats(selected_category, games_played, games_won, games_lost, total_guesses)