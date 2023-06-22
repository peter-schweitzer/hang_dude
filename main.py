#!/bin/python3

# Importieren von benötigten Modulen
from math import floor
from random import random
from typing import List, Literal


# ANSII escape sequences für farbigen Text
class text_color:
  BLUE: str = "\033[94m"
  CYAN: str = "\033[96m"
  GREEN: str = "\033[92m"
  ORANGE: str = "\033[93m"
  END: str = "\033[0m"


# mögliche Zustände der State-Machine
class States:
  done: int = -1
  main_menu: int = 0
  settings: int = 1
  guess_num: int = 2
  custom_word: int = 3
  enter_custom_word: int = 4
  playing: int = 5


# alle Buchstaben
alph: str = "abcdefghijklmnopqrstuvwxyz"


# Helferfunktion für Warnungen
def WRN(s: str) -> None:
  print(f"{text_color.ORANGE}{s}{text_color.END}")


# Helferfunktion für unerwartete Eingaben
def UE():
  WRN("Unerwartete Eingabe")


# Variablen vorbereiten
state: int = States.main_menu

default_guesses: int = 10
max_guesses: int = default_guesses
guesses: int = 0
guessed_chars: "List[str]" = []

use_random_word: bool = True
words: "List[str]" = []
word: str = ""

win = False

hung_dude = [
    '\n\n\n\n\n\n\n',
    '\n\n\n\n\n ꘍\n/ \\\n',
    '\n |\n |\n |\n |\n ꘍\n/ \\\n',
    ' ________\n |\n |\n |\n |\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |\n |\n |\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |\n |     []\n |\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |    \\\n |     []\n |\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |    \  /\n |     []\n |\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |    \  /\n |     []\n |    _/\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |    \  /\n |     []\n |    _/\\_\n ꘍\n/ \\\n',
    ' ________\n |     ||\n |    \\()/\n |     []\n |    _/\\_\n ꘍\n/ \\\n',
]  # nice


# Die texte die zu den entsprechenden Zuständen ausgegeben werden sollen (lambdas um interpolation jedes mal neu zu rendern)
prompts = [
    lambda: f"{text_color.CYAN}---Hauptmenu---{text_color.END}\n\n  {text_color.BLUE}1: (S)piel starten\n  2: (E)instellungen{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Einstellungen---{text_color.END}\n\n  {text_color.BLUE}1: (A)nzahl der Versuche\n  2: (W)ort festlegen oder zufällig wählen{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Anzahl Der Versuche---{text_color.END}\n\n  {text_color.BLUE}bitte eine Zahl zwischen 0-25 oder 's' für Standart (Standartwert ist 10, momentan {max_guesses}){text_color.END}\n",
    lambda: f"{text_color.CYAN}---Wort Festlegen Oder Zufällig Wählen---{text_color.END}\n\n  {text_color.BLUE}1: (Z)ufälliges Wort {'(momentan)' if use_random_word else '' }\n  2: (W)ort Festlegen/Multiplayer {'' if use_random_word else '(momentan)' }{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Wort Festlegen---{text_color.END}\n\n  {text_color.BLUE}Das Wort muss mehr als einen Buchstaben haben{text_color.END}\n",
    lambda: f"schon geratene Buchstaben:\n  {' '.join([(text_color.BLUE + c + text_color.END) if c in guessed_chars else '_' for c in alph])}\n\n  {guesses} von {max_guesses} falschen Versuchen\n  {['', '[' + '='*(guesses)+'>'+' '*(max_guesses-1-guesses)+']'][max_guesses == 10]}\n\n\n  {' '.join([(text_color.BLUE + c + text_color.END) if c in guessed_chars else '_' for c in word.lower()])}\n\n  {text_color.CYAN}Buchstabe oder Komplettlösung:{text_color.END}\n",
    lambda: f"Du hast {'GEWONNEN :)' if win else 'VERLOREN :('}\nDas Wort war '{word}'\n",
]


# Die Funktionen zu den entsprechenden Zuständen


def setup() -> None:
  print(f"{text_color.CYAN}====HANG-DUDE===={text_color.END}\n\n")


def main_menu(i: str) -> None:
  global state, guessed_chars

  if i == "q":
    exit(0)

  if i in ["s", "1"]:
    guessed_chars = []
    state = States.playing
  elif i in ["e", "2"]:
    state = States.settings
  else:
    UE()


def settings(i: str) -> None:
  global state

  if i == "q":
    state = States.main_menu
    return

  if i in ["1", "a"]:
    state = States.guess_num
  elif i in ["2", "w"]:
    state = States.custom_word
  else:
    UE()


def guess_num(i: str) -> None:
  global state, max_guesses, default_guesses

  if i == "q":
    state = States.settings
    return

  if i == "s":
    max_guesses = default_guesses
    state = States.settings
    return

  try:
    n = int(i, 10)
  except ValueError:
    WRN("Eingabe ist keine Zahl")
    return

  if n < 0 or n > 25:
    WRN("Eingabe ist eine ungültige Zahl")
    return

  max_guesses = n
  state = States.settings


def custom_word(i: str) -> None:
  global state, use_random_word

  if i == "q":
    state = States.settings
    return

  if i in ["1", "z"]:
    use_random_word = True
    state = States.settings
  elif i in ["2", "w"]:
    state = States.enter_custom_word
  else:
    UE()


def enter_custom_word(i: str) -> None:
  global state, word, use_random_word

  if i == "q":
    state = States.custom_word
  elif len(i) < 2:
    UE()
  else:
    word = i
    use_random_word = False
    state = States.settings


def playing(i: str) -> None:
  global state, word, max_guesses, guesses, win

  if i == ":q":
    state = States.main_menu

  elif len(i) == len(word):
    win = i == word.lower()
    state = States.done

  elif len(i) == 1:
    if i in guessed_chars:
      print("Buchstabe wurde bereits geraten")
      return

    guessed_chars.append(i)

    if not i in word.lower():
      guesses += 1
      if guesses == max_guesses:
        win = False
        state = States.done

  else:
    UE()

  if len([c for c in word.lower() if c in guessed_chars]) == len(word):
    win = True
    state = States.done


def done(_: str) -> "Literal[True]":
  return True


def main() -> None:
  global state, guesses, use_random_word, word, win, prompts

  guesses = 0
  state = States.main_menu
  win = False

  if use_random_word:
    with open("./deutsch.txt") as f:
      word = (lambda x: x[floor(random() * len(x))])(f.readlines())[:-1]

  else:
    state = States.enter_custom_word

  while True:
    print("\033[2J")
    if (state == States.playing or state == States.done) and max_guesses == 10:
      print(hung_dude[guesses])
    i = input(prompts[state]()).lower()
    if [
        main_menu,
        settings,
        guess_num,
        custom_word,
        enter_custom_word,
        playing,
        done,
    ][state](i):
      break


# Eintrittspunkt des Programms
if __name__ == "__main__":
  setup()
  main()
  while True:
    i = input(
        f"{text_color.GREEN}ERNEUT SPIELEN?{text_color.END}\n\n  {text_color.BLUE}1: (J)a\n  2: (N)ein{text_color.END}\n"
    ).lower()
    if i in ["", "1", "1", "j", "yes", "y", "ja"]:
      main()
    elif i in ["2", "2", "n", "q", "no", "nein"]:
      break
    else:
      UE()
