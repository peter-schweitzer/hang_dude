#!/bin/python3

from math import floor
from random import random
from typing import List, Literal


class text_color:
    BLUE: str = "\033[94m"
    CYAN: str = "\033[96m"
    GREEN: str = "\033[92m"
    WARN: str = "\033[93m"
    END: str = "\033[0m"


def WRN(s: str) -> None:
    print(f"{text_color.WARN}{s}{text_color.END}")


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


def main_menu(i: str) -> None:
    global state, guessed_chars

    if i == "q":
        exit(0)

    if i in ["s", "1", "1."]:
        guessed_chars = []
        state = States.playing
    elif i in ["e", "2", "2."]:
        state = States.settings
    else:
        WRN("Unerwartete Eingabe")


def settings(i: str) -> None:
    global state

    if i == "q":
        state = States.main_menu
        return

    if i in ["1", "1.", "a"]:
        state = States.guess_num
    elif i in ["2", "2.", "w"]:
        state = States.custom_word
    else:
        WRN("Unerwartete Eingabe")




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
