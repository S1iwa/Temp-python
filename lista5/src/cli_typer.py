import typer
import logging
import csv
import random
import statistics
from datetime import datetime
from pathlib import Path
from enum import Enum

from group_measurement_files_by_key import group_measurement_files_by_key

app = typer.Typer(help="Analiza danych GIOŚ z użyciem Typer")

# Logowanie
logger = logging.getLogger("Lab5_Typer")
logger.setLevel(logging.WARNING)
h_stdout = logging.StreamHandler()
h_stdout.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(h_stdout)


class Wielkosc(str, Enum):
    pm25 = "PM2.5"
    pm10 = "PM10"
    no = "NO"


class Czestotliwosc(str, Enum):
    h1 = "1g"
    h24 = "24g"


def wczytaj_tylko_stacje(sciezka):
    stacje = {}
    with open(sciezka, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stacje[row["Kod stacji"]] = row
    return stacje

def pobierz_dane(wielkosc, czestotliwosc, start_date, koniec_date, dir_path):
    try:
        stacje = wczytaj_tylko_stacje(dir_path / "stacje.csv")
    except Exception as e:
        typer.echo(f"Błąd krytyczny: {e}", err=True)
        raise typer.Exit(code=1)

    grupy = group_measurement_files_by_key(dir_path / "measurements")
    zebrane_pomiary = {}

    # PM2.5 -> PM25
    wielkosc_klucz = wielkosc.value.replace('.', '')

    for rok in range(start_date.year, koniec_date.year + 1):
        klucz = (str(rok), wielkosc_klucz, czestotliwosc.value)
        if klucz not in grupy:
            continue

        with grupy[klucz].open(encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=',')
            mapa_kolumn = {}

            for row_num, row in enumerate(reader):
                if not row:
                    continue

                if row_num == 1 and row[0] == "Kod stacji":
                    mapa_kolumn = {i: r.strip() for i, r in enumerate(row) if i > 0 and r.strip()}
                    continue

                if mapa_kolumn and row_num > 5:
                    data_str = row[0].strip().split()[0]
                    try:
                        if '/' in data_str:
                            dt = datetime.strptime(data_str, "%m/%d/%y").date()
                        elif '.' in data_str:
                            dt = datetime.strptime(data_str, "%d.%m.%Y").date()
                        else:
                            dt = datetime.strptime(data_str, "%Y-%m-%d").date()
                    except ValueError:
                        continue

                    if start_date <= dt <= koniec_date:
                        for idx, kod in mapa_kolumn.items():
                            if idx < len(row) and row[idx].strip():
                                try:
                                    wartosc = float(row[idx].replace(',', '.'))
                                    zebrane_pomiary.setdefault(kod, []).append(wartosc)
                                except ValueError:
                                    pass

    return stacje, zebrane_pomiary


@app.command()
def losowa_stacja(
        wielkosc: Wielkosc = typer.Option(..., help="Wielkość mierzona"),
        czestotliwosc: Czestotliwosc = typer.Option(..., help="Częstotliwość"),
        start: datetime = typer.Option(..., formats=["%Y-%m-%d"]),
        koniec: datetime = typer.Option(..., formats=["%Y-%m-%d"]),
        katalog: Path = typer.Option(Path("../data"), help="Katalog z danymi")):
    stacje, zebrane_pomiary = pobierz_dane(wielkosc, czestotliwosc, start.date(), koniec.date(), katalog)

    if not zebrane_pomiary:
        logger.warning("Brak pomiarów.")
        raise typer.Exit()

    wylosowana = random.choice(list(zebrane_pomiary.keys()))
    info = stacje.get(wylosowana, {})
    typer.echo(f"\n--- WYLOSOWANA STACJA ---")
    typer.echo(f"Kod: {wylosowana}")
    typer.echo(f"Nazwa: {info.get('Nazwa stacji', 'Brak')}")
    typer.echo(f"Pomiary: {len(zebrane_pomiary[wylosowana])}")


@app.command()
def statystyki(
        stacja: str = typer.Argument(..., help="Kod stacji (np. SkBuskRokosz)"),
        wielkosc: Wielkosc = typer.Option(...),
        czestotliwosc: Czestotliwosc = typer.Option(...),
        start: datetime = typer.Option(..., formats=["%Y-%m-%d"]),
        koniec: datetime = typer.Option(..., formats=["%Y-%m-%d"]),
        katalog: Path = typer.Option(Path("../data"))):
    _, zebrane_pomiary = pobierz_dane(wielkosc, czestotliwosc, start.date(), koniec.date(), katalog)

    if stacja not in zebrane_pomiary:
        logger.warning(f"Brak pomiarów dla stacji {stacja}.")
        raise typer.Exit()

    wartosci = zebrane_pomiary[stacja]
    srednia = statistics.mean(wartosci)
    odchylenie = statistics.stdev(wartosci) if len(wartosci) > 1 else 0.0

    typer.echo(f"\n--- STATYSTYKI ---")
    typer.echo(f"Stacja: {stacja}")
    typer.echo(f"Średnia: {srednia:.2f}")
    typer.echo(f"Odchylenie: {odchylenie:.2f}")


if __name__ == "__main__":
    app()