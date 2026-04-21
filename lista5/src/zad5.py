import argparse
from datetime import datetime


def waliduj_date(data_str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Niepoprawny format daty: {data_str}. Wymagany format to RRRR-MM-DD.")


def stworz_cli():
    parser = argparse.ArgumentParser(
        description="Interfejs linii komend do analizy danych pomiarowych zanieczyszczeń powietrza.")

    # Argumenty główne (wspólne, podlegające walidacji)
    parser.add_argument("--wielkosc", required=True, choices=['PM2.5', 'PM10', 'NO'], help="Mierzona wielkość")
    parser.add_argument("--czestotliwosc", required=True, choices=['1g', '24g'], help="Częstotliwość pomiarów")
    parser.add_argument("--start", required=True, type=waliduj_date, help="Początek przedziału czasowego (RRRR-MM-DD)")
    parser.add_argument("--koniec", required=True, type=waliduj_date, help="Koniec przedziału czasowego (RRRR-MM-DD)")

    # Konfiguracja podkomend
    subparsers = parser.add_subparsers(dest="komenda", required=True, help="Dostępne operacje")

    # Podkomenda 1: Wypisanie losowej stacji
    subparsers.add_parser("losowa-stacja", help="Wypisuje nazwę i adres losowej stacji dla podanych parametrów")

    # Podkomenda 2: Obliczanie statystyk
    parser_statystyki = subparsers.add_parser("statystyki", help="Oblicza średnią i odchylenie standardowe dla stacji")
    parser_statystyki.add_argument("--stacja", required=True, help="Nazwa lub identyfikator stacji pomiarowej")

    return parser


def main():
    parser = stworz_cli()
    args = parser.parse_args()


if __name__ == "__main__":
    main()