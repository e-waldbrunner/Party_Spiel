import random

spieler = []
aufgaben = [
    "Erzähle eine peinliche Geschichte!",
    "Mache 10 Liegestütze!",
    "Sing ein Lied!",
    "Imitiere einen Promi!"
]

def spieler_hinzufuegen():
    while True:
        name = input("Spielername (oder Enter zum Beenden): ")
        if name == "":
            break
        spieler.append(name)

def spiel_starten():

    if len(spieler) < 1:
        print("Keine Spieler vorhanden!")
        return

    while True:
        try:
            eingabe = input("Anzahl der Runden: ")

            if eingabe == "":
                print("Standardwert 1 wird benutzt.")
                anzahl_runden = 1
                break

            anzahl_runden = int(eingabe)

            if anzahl_runden <= 0:
                print("Bitte eine Zahl größer als 0 eingeben.")
                continue

            if anzahl_runden > 20:
                print("Bitte eine Zahl kleiner als 21 eingeben.")
                continue

            break

        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    for gespielte_runden in range(anzahl_runden):
        print("-------------------------")
        print(f"Runde: {gespielte_runden + 1} / {anzahl_runden}")

        for s in spieler:
            aufgabe = random.choice(aufgaben)
            print(f"\n{s} muss: {aufgabe}\n")
            fertig = input("Drücke Enter für den nächsten Spieler...")
            if fertig == "":
                continue


def menue():
    while True:
        print("-------------------------")
        print("1. Spieler hinzufügen")
        print("2. Spiel starten")
        print("3. Beenden")
        print("-------------------------")

        wahl = input("> ")

        if wahl == "1":
            spieler_hinzufuegen()
        elif wahl == "2":
            spiel_starten()
        elif wahl == "3":
            print("Spiel beendet.")
            break
        else:
            print("Ungültige Eingabe!")

menue()