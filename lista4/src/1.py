import os
import sys


def main():
    # Pobranie argumentów z linii komend (bez nazwy skryptu)
    args = sys.argv[1:]
    args = [arg.lower() for arg in args]

    # Pobieranie zmiennych środowiskowwych
    env_vars = os.environ

    # Filtruje zmienne jeśli są argumenty
    if args:
        filtered = {
            key: value
            for key, value in env_vars.items()
            if any(arg == key.lower() for arg in args) # Sprawdzenie czy dany klucz został podany jako argument
        }
    else:
        filtered = env_vars

    # Sortowanie po kluczu
    for key in sorted(filtered):
        print(f"{key}={filtered[key]}")


if __name__ == "__main__":
    main()