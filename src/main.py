def main():
    nazwa_zespolu = "Pythonuhy"
    czlonkowie = ["Michał Śliwa", "Miłosz Przybył"]

    print(f"Nazwa zespołu: {nazwa_zespolu}")
    print(f"Nazwa członkowie:")
    for osoba in czlonkowie:
        print(f"- {osoba}")

    print("Program został uruchomiony poprawnie...")

if __name__ == "__main__":
    main()