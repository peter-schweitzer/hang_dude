#!/bin/python3

from math import floor
from random import random


alph = "abcdefghijklmnopqrstuvwxyz"

default_guesses: int = 10
max_guesses: int = default_guesses
guesses: int = 0
guessed_chars: "List[str]" = []

use_random_word: bool = True
words: "List[str]" = []
word: str = ""

win = False


class States:
    done: int = -1
    main_menu: int = 0
    settings: int = 1
    guess_num: int = 2
    custom_word: int = 3
    enter_custom_word = 4
    playing: int = 5


state: int = States.main_menu
prompts = [
    lambda: f"{text_color.CYAN}---Hauptmenu---{text_color.END}\n\n  {text_color.BLUE}1: (S)piel starten\n  2: (E)instellungen{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Einstellungen---{text_color.END}\n\n  {text_color.BLUE}1: (A)nzahl der Versuche\n  2: (W)ort festlegen oder zufällig wählen{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Anzahl Der Versuche---{text_color.END}\n\n  {text_color.BLUE}bitte eine Zahl zwischen 0-25 oder 's' für Standart (Standartwert ist 10, momentan {max_guesses}){text_color.END}\n",
    lambda: f"{text_color.CYAN}---Wort Festlegen Oder Zufällig Wählen---{text_color.END}\n\n  {text_color.BLUE}1: (Z)ufälliges Wort {'(momentan)' if use_random_word else '' }\n  2: (W)ort Festlegen/Multiplayer {'' if use_random_word else '(momentan)' }{text_color.END}\n",
    lambda: f"{text_color.CYAN}---Wort Festlegen---{text_color.END}\n\n  {text_color.BLUE}Das Wort muss mehr als einen Buchstaben haben{text_color.END}\n",
    lambda: f"schon geratene Buchstaben:\n  {' '.join(map(lambda c: ''.join([text_color.BLUE, c, text_color.END]) if c in guessed_chars else '_', alph))}\n{guesses} von {max_guesses} falschen Versuchen\n\n{' '.join(map(lambda c: ''.join([text_color.BLUE, c, text_color.END]) if c in guessed_chars else '_', word))}\n\n{text_color.CYAN}Buchstabe oder Komplettlösung:{text_color.END}\n",
    lambda: f"Du hast {'GEWONNEN :)' if win else 'VERLOREN :('}\n",
]


def setup() -> None:
    print(f"{text_color.CYAN}====HANG-DUDE===={text_color.END}\n\n")


def main_menu():
  print("mein_menu W.I.P")


def playing():
  print("mein_menu W.I.P")


def done(_: str) -> "Literal[True]":
    return True


def main() -> None:
    while True:
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


if __name__ == "__main__":
    setup()
    main()
    while True:
        i = input(f"{text_color.GREEN}ERNEUT SPIELEN? [J/n]{text_color.END}").lower()
        if i in ["yes", "y", "ja", "j", ""]:
            main()
        elif i in ["q", "no", "n", "nein"]:
            break
