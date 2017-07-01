# -*- coding: UTF-8 -*-

#SPECIAL THANKS:
#ÁDÁM FOR THE GAME IDEA AND LETTING ME OVERCOMPLICATE IT
#EASY AND MEDIUM WORDS FROM: https://www.thegamegal.com/printables/
#HARD WORDS FROM: https://www.hangmanwords.com/words
#COLORED TEXT: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

#IMPORT

from __future__ import print_function
import random

#WORDS

easy_words = [
  "airplane", 
  "alligator", 
  "ant", 
  "arm", 
  "baby", 
  "back", 
  "balloon", 
  "baseball", 
  "basketball", 
  "bat", 
  "bear", 
  "bell", 
  "bike", 
  "bird", 
  "blink", 
  "blocks", 
  "bone", 
  "book", 
  "bowl", 
  "bracelet", 
  "branch", 
  "bread", 
  "bunny", 
  "bus", 
  "camera", 
  "car", 
  "carrot", 
  "chair", 
  "cheek", 
  "cherry", 
  "chicken", 
  "circle", 
  "clap", 
  "clock", 
  "cloud", 
  "corn", 
  "crab", 
  "cupcake", 
  "dance", 
  "dinosaur", 
  "dog", 
  "doll", 
  "door", 
  "draw", 
  "drink", 
  "ear", 
  "ears", 
  "eat", 
  "elephant", 
  "football", 
  "giraffe", 
  "glasses", 
  "grapes", 
  "grass", 
  "happy", 
  "head", 
  "hopscotch", 
  "horse", 
  "inchworm", 
  "jellyfish", 
  "jump", 
  "kangaroo", 
  "kick", 
  "lamp", 
  "leaf", 
  "lollipop", 
  "monkey", 
  "moon", 
  "mosquito", 
  "mouth", 
  "orange", 
  "pen", 
  "pencil", 
  "pig", 
  "pillow", 
  "pinch", 
  "point", 
  "prayer", 
  "purse", 
  "ring", 
  "robot", 
  "rocket", 
  "scissors", 
  "seashell", 
  "shark", 
  "skip", 
  "sleep", 
  "smile", 
  "snail", 
  "sneeze", 
  "snowman", 
  "spider", 
  "stop", 
  "tail", 
  "telephone", 
  "toothbrush", 
  "truck", 
  "turtle", 
  "wave", 
  "bridge", 
]
medium_words = [
  "aircraft",
  "artist", 
  "backbone", 
  "barn", 
  "base", 
  "baseball", 
  "battery", 
  "beach", 
  "beaver", 
  "beehive", 
  "bib", 
  "bicycle", 
  "birthday", 
  "blowfish", 
  "bomb", 
  "boot", 
  "bottle", 
  "bowtie", 
  "brain", 
  "bubble", 
  "cake", 
  "camera", 
  "cello", 
  "chalk", 
  "cheek", 
  "cheeseburger", 
  "chin", 
  "circus", 
  "clam", 
  "coal", 
  "coconut", 
  "computer", 
  "corner", 
  "cowboy", 
  "crib", 
  "deep", 
  "desk", 
  "doghouse", 
  "dollar", 
  "dominoes", 
  "door", 
  "doormat", 
  "easel", 
  "electricity", 
  "face", 
  "fang", 
  "fist", 
  "flagpole", 
  "flashlight", 
  "flute", 
  "frog", 
  "fur", 
  "garbage", 
  "garden", 
  "gate", 
  "half", 
  "happy", 
  "hippopotamus", 
  "hockey", 
  "hook", 
  "hopscotch", 
  "horse", 
  "ice", 
  "key", 
  "knee", 
  "lawnmower", 
  "lighthouse", 
  "lightsaber", 
  "lobster", 
  "mail", 
  "mailman", 
  "mattress", 
  "mitten", 
  "money", 
  "muffin", 
  "mushroom", 
  "music", 
  "nail", 
  "nature", 
  "newspaper", 
  "outside", 
  "owl", 
  "pajamas", 
  "palace", 
  "park", 
  "password", 
  "peach", 
  "peanut", 
  "pelican", 
  "pencil", 
  "photograph", 
  "pineapple", 
  "pinwheel", 
  "pirate", 
  "plate", 
  "platypus", 
  "poodle", 
  "popcorn", 
  "popsicle", 
  "potato", 
  "pretzel", 
  "purse", 
  "queen", 
  "quilt", 
  "radish", 
  "rain", 
  "rainbow", 
  "ring", 
  "round", 
  "rug", 
  "sailboat", 
  "school", 
  "seahorse", 
  "seesaw", 
  "shallow", 
  "shark", 
  "sheep", 
  "silverware", 
  "skate", 
  "ski", 
  "skirt", 
  "snowball", 
  "snowflake", 
  "soda", 
  "song", 
  "spare", 
  "spine", 
  "spool", 
  "spoon", 
  "spring", 
  "sprinkler", 
  "state", 
  "stingray", 
  "stomach", 
  "stoplight", 
  "storm", 
  "suitcase", 
  "sunflower", 
  "swing", 
  "teapot", 
  "telephone", 
  "thief", 
  "ticket", 
  "toast", 
  "toe", 
  "treasure", 
  "trip", 
  "tusk", 
  "waist", 
  "wax", 
  "whisk", 
  "whistle", 
]
hard_words = [
  "abruptly", 
  "absurd", 
  "abyss", 
  "affix", 
  "askew", 
  "avenue", 
  "awkward", 
  "axiom", 
  "azure", 
  "bagpipes", 
  "bandwagon", 
  "banjo", 
  "bayou", 
  "beekeeper", 
  "bikini", 
  "blitz", 
  "blizzard", 
  "boggle", 
  "bookworm", 
  "boxcar", 
  "boxful", 
  "buckaroo", 
  "buffalo", 
  "buffoon", 
  "buxom", 
  "buzzard", 
  "buzzing", 
  "buzzwords", 
  "caliph", 
  "cobweb", 
  "cockiness", 
  "croquet", 
  "crypt", 
  "curacao", 
  "cycle", 
  "daiquiri", 
  "dirndl", 
  "disavow", 
  "dizzying", 
  "duplex", 
  "dwarves", 
  "embezzle", 
  "equip", 
  "espionage", 
  "euouae", 
  "exodus", 
  "faking", 
  "fishhook", 
  "fixable", 
  "fjord", 
  "flapjack", 
  "flopping", 
  "fluffiness", 
  "flyby", 
  "foxglove", 
  "frazzled", 
  "frizzled", 
  "fuchsia", 
  "funny", 
  "gabby", 
  "galaxy", 
  "galvanize", 
  "gazebo", 
  "giaour", 
  "gizmo", 
  "glowworm", 
  "glyph", 
  "gnarly", 
  "gnostic", 
  "gossip", 
  "grogginess", 
  "haiku", 
  "haphazard", 
  "hyphen", 
  "iatrogenic", 
  "icebox", 
  "injury", 
  "ivory", 
  "ivy", 
  "jackpot", 
  "jaundice", 
  "jawbreaker", 
  "jaywalk", 
  "jazziest", 
  "jazzy", 
  "jelly", 
  "jigsaw", 
  "jinx", 
  "jiujitsu", 
  "jockey", 
  "jogging", 
  "joking", 
  "jovial", 
  "joyful", 
  "juicy", 
  "jukebox", 
  "jumbo", 
  "kayak", 
  "kazoo", 
  "keyhole", 
  "khaki", 
  "kilobyte", 
  "kiosk", 
  "kitsch", 
  "kiwifruit", 
  "klutz", 
  "knapsack", 
  "larynx", 
  "lengths", 
  "lucky", 
  "luxury", 
  "lymph", 
  "marquis", 
  "matrix", 
  "megahertz", 
  "microwave", 
  "mnemonic", 
  "mystify", 
  "naphtha", 
  "nightclub", 
  "nowadays", 
  "numbskull", 
  "nymph", 
  "onyx", 
  "ovary", 
  "oxidize", 
  "oxygen", 
  "pajama", 
  "peekaboo", 
  "phlegm", 
  "pixel", 
  "pizazz", 
  "pneumonia", 
  "polka", 
  "pshaw", 
  "psyche", 
  "puppy", 
  "puzzling", 
  "quartz", 
  "queue", 
  "quips", 
  "quixotic", 
  "quiz", 
  "quizzes", 
  "quorum", 
  "razzmatazz", 
  "rhubarb", 
  "rhythm", 
  "rickshaw", 
  "schnapps", 
  "scratch", 
  "shiv", 
  "snazzy", 
  "sphinx", 
  "spritz", 
  "squawk", 
  "staff", 
  "strength", 
  "strengths", 
  "stretch", 
  "stronghold", 
  "stymied", 
  "subway", 
  "swivel", 
  "syndrome", 
  "thriftless", 
  "thumbscrew", 
  "topaz", 
  "transcript", 
  "transgress", 
  "transplant", 
  "triphthong", 
  "twelfth", 
  "twelfths", 
  "unknown", 
  "unworthy", 
  "unzip", 
  "uptown", 
  "vaporize", 
  "vixen", 
  "vodka", 
  "voodoo", 
  "vortex", 
  "voyeurism", 
  "walkway", 
  "waltz", 
  "wave", 
  "wavy", 
  "waxy", 
  "wellspring", 
  "wheezy", 
  "whiskey", 
  "whizzing", 
  "whomever", 
  "wimpy", 
  "witchcraft", 
  "wizard", 
  "woozy", 
  "wristwatch", 
  "wyvern", 
  "xylophone", 
  "yachtsman", 
  "yippee", 
  "yoked", 
  "youthful", 
  "yummy", 
  "zephyr", 
  "zigzag", 
  "zigzagging", 
  "zilch", 
  "zipper", 
  "zodiac", 
  "zombie"
]

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
#class color:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'

#HANGMANIMATION

hangman_states = [
  ["",              "",             "",               "",             "",              "",   "_____________"],
  ["",              "",             "",               "",             "",              "",   "_⏊___________"],
  [" |",            " |",           " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |",           " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |",             " |",           " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |        |",    " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |      / |",    " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |      / | \\", " |        |",  " |",            " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |      / | \\", " |        |",  " |        /",   " |", "_⏊___________"],
  [" ⎾‾‾‾‾‾‾‾‾⏋", " |        😀", " |      / | \\", " |        |",  " |        /\\", " |", "_⏊___________"]
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
  
#MAIN LOGIC

header("Welcome to the Ultimate Hangman " + version)
choose_difficulty()
while True:
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
