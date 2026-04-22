import argparse
import logging
import sys
import random
import statistics
import csv
from datetime import datetime
from pathlib import Path

from group_measurement_files_by_key import group_measurement_files_by_key

def konfiguruj_logowanie():
    logger = logging.getLogger("Lab5")
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(levelname)s: %(message)s')

    class StdoutFilter(logging.Filter):
        def filter(self, record):
            return record.levelno <= logging.WARNING

    stdout = logging.StreamHandler(sys.stdout)
    stdout.addFilter(StdoutFilter())
    stdout.setFormatter(fmt)
    logger.addHandler(stdout)

    stderr = logging.StreamHandler(sys.stderr)
    stderr.setLevel(logging.ERROR)
    stderr.setFormatter(fmt)
    logger.addHandler(stderr)
    return logger


def waliduj_date(data_str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Zły format: {data_str}. Wymagany RRRR-MM-DD")

def wczytaj_tylko_stacje(sciezka):
    stacje = {}
    with open(sciezka, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stacje[row["Kod stacji"]] = row
    return stacje

def main():
    logger = konfiguruj_logowanie()

    parser = argparse.ArgumentParser()
    parser.add_argument("--wielkosc", required=True, choices=['PM2.5', 'PM10', 'NO'])
    parser.add_argument("--czestotliwosc", required=True, choices=['1g', '24g'])
    parser.add_argument("--start", required=True, type=waliduj_date)
    parser.add_argument("--koniec", required=True, type=waliduj_date)
    parser.add_argument("--dir", default="../data", help="Katalog z danymi")

    subparsers = parser.add_subparsers(dest="komenda", required=True)
    subparsers.add_parser("losowa-stacja")
    p_stat = subparsers.add_parser("statystyki")
    p_stat.add_argument("--stacja", required=True)

    args = parser.parse_args()
    dir_path = Path(args.dir)

    try:
        sciezka_stacje = dir_path / "stacje.csv"
        stacje = wczytaj_tylko_stacje(sciezka_stacje)
    except Exception as e:
        logger.error(f"Błąd krytyczny podczas wczytywania stacji: {e}")
        sys.exit(1)

    katalog_pomiary = dir_path / "measurements"
    if not katalog_pomiary.exists():
        logger.error("Brak katalogu measurements")
        sys.exit(1)

    grupy = group_measurement_files_by_key(katalog_pomiary)
    zebrane_pomiary = {}
    znaleziono_plik = False

    for rok in range(args.start.year, args.koniec.year + 1):
        wielkosc_klucz = args.wielkosc.replace('.', '')
        klucz = (str(rok), wielkosc_klucz, args.czestotliwosc)
        if klucz not in grupy:
            continue

        znaleziono_plik = True
        sciezka_pliku = grupy[klucz]

        logger.info(f"Otwieranie pliku: {sciezka_pliku.name}")
        try:
            with sciezka_pliku.open(encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=',')

                mapa_kolumn = {}

                for row_num, row in enumerate(reader):
                    # Pomijamy puste wiersze
                    if not row:
                        continue

                    bajt_wiersza = len(",".join(row).encode('utf-8'))
                    logger.debug(f"Przeczytano bajtów: {bajt_wiersza}")

                    if row_num == 1 and row[0] == "Kod stacji":
                        for i in range(1, len(row)):
                            if row[i].strip():
                                mapa_kolumn[i] = row[i].strip()
                        continue

                    if mapa_kolumn and row_num > 5:
                        data_str = row[0].strip().split()[0]

                        try:
                            if '/' in data_str:
                                data_wiersza = datetime.strptime(data_str, "%m/%d/%y").date()
                            elif '.' in data_str:
                                data_wiersza = datetime.strptime(data_str, "%d.%m.%Y").date()
                            else:
                                data_wiersza = datetime.strptime(data_str, "%Y-%m-%d").date()
                        except ValueError:
                            continue

                        if args.start <= data_wiersza <= args.koniec:
                            for idx, kod_stacji in mapa_kolumn.items():
                                if idx < len(row) and row[idx].strip():
                                    wartosc_str = row[idx].replace(',', '.').strip()
                                    try:
                                        wartosc = float(wartosc_str)
                                        if kod_stacji not in zebrane_pomiary:
                                            zebrane_pomiary[kod_stacji] = []
                                        zebrane_pomiary[kod_stacji].append(wartosc)
                                    except ValueError:
                                        pass

            logger.info(f"Zamykanie pliku: {sciezka_pliku.name}")
        except Exception as e:
            logger.error(f"Błąd odczytu pliku {sciezka_pliku.name}: {e}")

    if not znaleziono_plik:
        logger.warning(f"Użytkownik podał mierzoną wielkość, która nie występuje w plikach: {args.wielkosc}")

    if not zebrane_pomiary:
        logger.warning("Brak dostępnych pomiarów dla zadanych parametrów.")
        sys.exit(0)

    if args.komenda == 'losowa-stacja':
        wylosowana = random.choice(list(zebrane_pomiary.keys()))
        info = stacje.get(wylosowana, {})
        print(f"Losowa stacja: {info.get('Nazwa stacji', wylosowana)}")
        print(f"Adres: {info.get('Adres', 'Brak')}")

    elif args.komenda == 'statystyki':
        if args.stacja not in zebrane_pomiary:
            logger.warning(f"Częstotliwość lub wielkość nie jest wspierana przez daną stację ({args.stacja}).")
            sys.exit(0)

        wartosci = zebrane_pomiary[args.stacja]
        srednia = statistics.mean(wartosci)
        odchylenie = statistics.stdev(wartosci) if len(wartosci) > 1 else 0.0

        print(f"Stacja: {args.stacja}")
        print(f"Średnia: {srednia:.2f}")
        print(f"Odchylenie: {odchylenie:.2f}")


if __name__ == "__main__":
    main()