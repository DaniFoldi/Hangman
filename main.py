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

#WORD LIST

word_list = []

#VERSION

version = "v1.4"

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
  ["",              "",             "",               "",             "",              "",   "_____________"],
  ["",              "",             "",               "",             "",              "",   "_⏊___________"],
  [" |",            " |",           " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |",           " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😂️", " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😄", " |        |",    " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |      / |",    " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        🙂", " |      / | \\", " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        🙁", " |      / | \\", " |        |",  " |        /",   " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😱", " |      / | \\", " |        |",  " |        /\\", " |", "_⏊___________"]
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
word_characters = []
word_guessed = []
lives_left = 0

#FUNCTIONS

def reset_word():
  global word_guessed
  word_guessed = []
  for i in range(0, len(word)):
    word_guessed.append("_")

def reset_game():
  global lives_left
  global word
  global word_characters
  global characters_guessed
  global word_guessed
  lives_left = 10
  word = ""
  word_characters = []
  characters_guessed = []

def choose_word():
  global word
  global word_characters
  if selected_difficulty in difficulties:
    word = word_list[random.randint(0, len(word_list) - 1)]
    word_characters = list(word)
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
  asd = 5

def win():
  for char in word_guessed:
    if char == "_":
      return False
  return True
  
def guess_letter():
  global characters_guessed
  global word_characters
  global lives_left
  global word_guessed
  print("Please input your guess")
  char = input("")
  char = char.lower()
  if char not in alphabet:
    error("Incorrect guess")
    guess_letter()
  else:
    if char in characters_guessed:
      error("Letter already guessed")
      guess_letter()
    else:
      char_in_word = False
      for i in range(0, len(word_characters)):
        if word_characters[i] == char:
          word_guessed[i] = char
          char_in_word = True
      if not char_in_word:
        lives_left -= 1
      characters_guessed.append(char)
  
def print_lives():
  print("Lives: " + str(lives_left))

def print_stats():
  print("Difficulty: " + color.green + selected_difficulty+ color.end)
  print("Games played: " + color.green + str(games_played)+ color.end)
  print("Games won: " + color.green + str(games_won)+ color.end)
  print("Games lost: " + color.green + str(games_lost)+ color.end)
  if games_lost == 0:
    print("W/L Ratio: " + color.green + "-" + color.end)
  else:
    print("W/L Ratio: " + color.green + str(games_won / games_lost)+ color.end)
  
def print_word():
  for i in range(0, len(word_guessed)):
    print(word_guessed[i], end = "")
    if i < len(word_guessed):
      print(" ", end = "")
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
    for i in range(0, len(hangman_states[0])):
      print(hangman_states[lives_max - 1 - lives_left][i])
  
def choose_difficulty():
  global selected_difficulty
  print("Please select a difficulty level: ")
  for i in range(0, len(difficulties)):
    print(color.green + difficulties[i] + color.end, end = "")
    if i < len(difficulties) - 1:
      print(" / ", end = "")
  print()
  selected_difficulty = input("")
  selected_difficulty = selected_difficulty.capitalize()
  if selected_difficulty not in difficulties:
    error("Difficulty not available")
    choose_difficulty()
  else:
    with open((selected_difficulty + ".csv"), newline = "") as word_file:
      reader =  csv.reader(word_file, delimiter = " ", quotechar = "|")
      for option in reader:
        word_list.append(option[0])
    print(word_list)

  
#MAIN LOGIC
if __name__ == "__main__":
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
    print_stats()
