import os
import argparse


def list_paths():
    path = os.environ.get("PATH", "")
    dirs = path.split(os.pathsep)

    for d in dirs:
        print(d)


def list_executables():
    path = os.environ.get("PATH", "")
    dirs = path.split(os.pathsep)

    for d in dirs:
        print(f"\n[{d}]")
        if os.path.isdir(d):
            try:
                for file in os.listdir(d):
                    full_path = os.path.join(d, file)

                    # Sprawdzanie czy plik jest wykonywalny
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(file)
            except PermissionError:
                print("Brak dostępu")
        else:
            print("Nie istnieje")


def main():
    parser = argparse.ArgumentParser(description="Operacje na zmiennej PATH")
    parser.add_argument("--list", action="store_true", help="Lista katalogów PATH")
    parser.add_argument("--exec", action="store_true", help="Lista plików wykonywalnych")

    args = parser.parse_args()

    if args.list:
        list_paths()
    elif args.exec:
        list_executables()
    else:
        print("Podaj parametr: --list lub --exec")


if __name__ == "__main__":
    main()