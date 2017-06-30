#IMPORT

import random

#WORDS

easy_words = ["apple", "banana", "cherry", "door", "empire", "forest", "gnome", "house", "impressive", "joke", "knowledge", "lamb", "milestone"]
medium_words = ["computer"]
hard_words = ["shelf"]

#HANGMANIMATION

hangman_states = [
  ["",              "",             "",                 "",              "",               "", "_____________"],
  ["",              "",             "",                 "",              "",               "", "_⏊___________"],
  [" |",            " |",           " |",               " |",            " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |",            " |",              " |",            " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |",              " |",            " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |         |",    " |         |",  " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |       / |",    " |         |",  " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |       / | \\", " |         |",  " |",             " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |       / | \\", " |         |",  " |         /",   " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |         😀", " |       / | \\", " |         |",  " |         /\\", " |", "_⏊___________"]
  ]


#STATS

games_played = 0
games_won = 0
games_lost = 0

#DIFFICULTIES

difficulties = ["easy", "medium", "hard"]

#alphabet

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
  if selected_difficulty == difficulties[0]:
    word = easy_words[random.randint(0, len(easy_words) - 1)]
    word_characters = list(word)
    reset_word()
  elif selected_difficulty == difficulties[1]:
    word = medium_words[random.randint(0, len(medium_words) - 1)]
    word_characters = list(word)
    reset_word()
  elif selected_difficulty == difficulties[2]:
    word = hard_words[random.randint(0, len(hard_words) - 1)]
    word_characters = list(word)
    reset_word
  else:
    print("Incorrect difficulty selected")
    choose_difficulty()
    choose_word()

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
  if char not in alphabet:
    print("Incorrect guess")
    guess_letter()
  else:
    if char in characters_guessed:
      print("Letter already guessed")
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
  print("Difficulty: " + selected_difficulty)
  print("Games played: " + str(games_played))
  print("Games won: " + str(games_won))
  print("Games lost: " + str(games_lost))
  if games_lost == 0:
    print("W/L Ratio: -")
  else:
    print("W/L Ratio: " + str(games_won / games_lost))
  
def print_word():
  for i in range(0, len(word_guessed)):
    print(word_guessed[i], end = "")
    if i < len(word_guessed):
      print(" ", end = "")
  print()
  
def print_state():
  hangman_state()
  print_lives()
  print_word()
  
def lose():
  if lives_left <= 0:
    return True
  else:
    return False

def hangman_state():
  if lives_left < 10:
    for i in range(0, len(hangman_states[0])):
      print(hangman_states[9 - lives_left][i])
  
def choose_difficulty():
  global selected_difficulty
  print("Please select a difficulty level: easy / medium / hard")
  selected_difficulty = input("")
  if selected_difficulty not in difficulties:
    print("Difficulty not available")
    choose_difficulty()
  
#MAIN LOGIC

print("Welcome to the Ultimage Hangman v1.2.")
choose_difficulty()
while True:
  reset_game()
  choose_word()
  print_state()
  
  while not(win() or lose()):
    guess_letter()
    print_state()
    
  if win():
    print("You won the game! Congrats!")
    games_won += 1
    games_played += 1
  elif lose():
    print("You lost.")
    print("The word was: " + word)
    games_lost += 1
    games_played += 1
  print_stats()
