import re
import unicodedata
import csv

def load_metadata(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        return list(reader)

def remove_diacritics(text):
    # unicodedata wiekszosc polskich znakow zamienia na na litere + ogonek np na ą na a + coś
    # a nie robi tego z ł bo jest idk upośledzone
    # i potem następnie z Mn usuwamy to przez co zamienia polskie znaki na zwykłe bez ogonków
    text = text.replace(' ', '_').replace('ł', 'l').replace('Ł', 'L')
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def analyze_stations(stations_data):
    for row in stations_data:
        row_text = " ".join(row.values())
        print(row_text)

        # a
        dates_target = f"{row.get('Data uruchomienia', '')} {row.get('Data zamknięcia', '')}"
        dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', dates_target)
        print(dates)

        # b
        coords = re.findall(r'\b\d+\.\d{6}\b', row_text)
        print(coords)

        # c
        station_name = row.get('Nazwa stacji', '')
        two_parts = bool(re.fullmatch(r'[^-]+-[^-]+', station_name))
        print(two_parts)

        # d
        clean_name = remove_diacritics(station_name)
        print(clean_name)

        # e
        kod = row.get('Kod stacji', '')
        rodzaj = row.get('Rodzaj stacji', '')
        is_valid_mob = not (kod.endswith('MOB') and rodzaj.lower() != 'mobilna')
        print(is_valid_mob)

        # f
        three_parts = bool(re.fullmatch(r'[^-]+-[^-]+-[^-]+', station_name))
        print(three_parts)

        # g
        has_street = bool(re.search(r',.*\b(?:ul\.|al\.)', row_text, re.IGNORECASE))
        print(has_street)

if __name__ == '__main__':
    stations_data = load_metadata('../data/stacje.csv')
    analyze_stations(stations_data)