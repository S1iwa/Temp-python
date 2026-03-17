import src.functions as fnc


def main():
    nazwa_zespolu = "Pythonuhy"
    czlonkowie = ["Michał Śliwa", "Miłosz Przybył"]

    print(f"Nazwa zespołu: {nazwa_zespolu}")
    print(f"Nazwa członkowie:")
    for osoba in czlonkowie:
        print(f"- {osoba}")

    print("Program został uruchomiony poprawnie...")

    print(fnc.countMembers(czlonkowie))
    print(fnc.formatGreeting(nazwa_zespolu))
    fnc.printMembers(czlonkowie)


if __name__ == "__main__":
    main()