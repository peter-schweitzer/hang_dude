state: int = 0
words: "list[str]" = []
word: str = ""


def setup() -> None:
  print("W.I.P")


def main_menu():
  print("mein_menu W.I.P")


def playing():
  print("mein_menu W.I.P")


def done():
  print("done W.I.P")


def main() -> None:
  while True:
    i = input().lower()
    [main_menu, playing, done][state]()


if __name__ == "__main__":
  setup()
  main()
  while True:
    i = input("ERNEUT SPIELEN? [J/n]").lower()
    if i in ["yes", "y", "ja", "j"]:
      main()
    elif i in ["no", "n", "nein"]:
      break
