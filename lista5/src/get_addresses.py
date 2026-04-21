import re
import csv
from pathlib import Path


def get_addresses(path: Path, city: str):
    result = []
    # ulica + opcjonalny numer
    pattern = re.compile(r"^(?:ul\.\s*)?(.*?)(?:\s+(\d+\w*))?$")

    with path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # pomijamy nagłówek (csv.reader skleja wieloliniowe pole w cudzysłowach)
        for parts in reader:
            if len(parts) < 13:
                continue

            # kolumny: 0=Nr, 10=Województwo, 11=Miejscowość, 12=Adres
            woj = parts[10].strip()
            miasto = parts[11].strip()
            adres = parts[12].strip()

            if miasto.lower() != city.lower():
                continue

            if not adres:
                result.append((woj, miasto, None, None))
                continue

            match = pattern.match(adres)
            if match:
                ulica = match.group(1).strip()
                numer = match.group(2)
                if numer:
                    result.append((woj, miasto, ulica, numer))
                else:
                    result.append((woj, miasto, ulica))

    return result


if __name__ == "__main__":
    path = Path("../data/stacje.csv")
    city = "Wrocław"
    addresses = get_addresses(path, city)
    for entry in addresses:
        print(entry)
