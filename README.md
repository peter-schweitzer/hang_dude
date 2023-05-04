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
- einstellen können, wieviele falsche Versuche man hat
- Wie oft wurtde schon falsch geraten / wie oft darf man falsch raten
- Option nach Ende erneut zu spielen
- Komplettlösung möglich

### Pflichten

- [Boilerplate & Main-Loop](#main-loop)
- [State-Machine designen](#state-machine)
  - mögliche Zustände:
    - Hauptmenu (main_menu)
    - am spielen (playing)
    - Einstellungen (settings)
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

#### playing

#### settings

### UI
