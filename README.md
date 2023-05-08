# SE - Galgenpersönchen

- [Planung](#Planung)
- [Umsetzung](#Umsetzung)
## Planung

### Anforderungen

- Konsolenbasiert
- Zufälliges oder vom einem Spieler eingegebenes Wort
- Länge des Wortes ist bekannt
- richtig erratene Buchstaben anzeigen
  - deren Position im Wort
  - Dopplungen beachten
- Welche Buchstben wurden schon geraten
- einstellen können, wieviele falsche Versuche man hat (Standart is 10)
- Wie oft wurtde schon falsch geraten / wie oft darf man falsch raten
- Option nach Ende erneut zu spielen
- Komplettlösung möglich

### Pflichten

- [Boilerplate & Main-Loop](#main-loop)
- [State-Machine designen](#state-machine)
  - mögliche Zustände:
    - Hauptmenu (main_menu)
    - Einstellungen (settings)
      - Anzahl der Versuche (guess_num)
      - Wort Festlegen Oder Zufällig Wählen (custom_word)
        - Eigenes Wort festlegen (enter_custom_name)
    - am spielen (playing)
  - wie werden diese Unterschieden
    - globale `state` Variable
- [Benutzeroberfläche](#ui)

## Umsetzung

### Main Loop

> beim Start des Programmes die main Funktion aufrufen

```py
if __name__ == "__main__":
  main()
```

> einfache `while True`-Schleife, aus der zum Ende ausgebrochen wird

```py
def main():
  while True:
    #die State-Machine
```

### State-Machine

#### main_menu

#### settings

#### playing

### UI

Mit "q" kann man ein Untermenu zurück gehen, außer im `playing` Zustand.

#### Multiple Choise

Optionen werden gelistet

```txt
---Menu-Titel---

1. (O)ption 1
2. (M)öglichkeit 2
```

Valide Eingaben für `Option 1` sind `1`, `1.`, `o` und `O`.
Valide Eingaben für `Möglichkeit 2` sind `2`, `2.`, `m` und `M`.

#### Texteingabe

Im `playing` Zustand wird eine Eingabe mit nur einem Textzeichen als einzelner Buchstabe gewertet.
Wenn die Eingabe die gleiche Länge wie das gesuchte Wort hat, wird es als Komplettlösung gewertet.
Alle anderen Eingaben werden als invalide angesehen und nicht gewwertet.

