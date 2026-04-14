import sys
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Prosty tail")

    parser.add_argument(
        "--lines",
        type=int,
        default=10,
        help="Liczba linii do wypisania (domyślnie 10)"
    )

    parser.add_argument(
        "--follow",
        action="store_true",
        help="Śledzi dopisywanie nowych linii"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Ścieżka do pliku (opcjonalna)"
    )

    return parser.parse_args()


def read_input(file_path):
    if file_path:
        try:
            with open(file_path, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Nie ma takiego pliku")
            sys.exit(1)
    else:
        return sys.stdin.readlines()


def tail(lines_data, n):
    return lines_data if len(lines_data) <= n else lines_data[-n:]


def follow_file(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)  # przejście na koniec pliku

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            print(line, end="")


def main():
    args = parse_args()

    # jeśli plik → ignorujemy stdin
    data = read_input(args.file)

    result = tail(data, args.lines)

    for line in result:
        print(line, end="")

    # follow działa tylko dla pliku
    if args.follow:
        if not args.file:
            print("\n--follow działa tylko z plikiem")
            sys.exit(1)

        follow_file(args.file)


if __name__ == "__main__":
    main()