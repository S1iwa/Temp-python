import re
from pathlib import Path


def group_measurement_files_by_key(path: Path) -> dict:
    result = {}

    # regex:
    # 1. rok: 4 cyfry
    # 2. wielkość: wszystko do następnego "_"
    # 3. częstotliwość: np. 24g, 1g itd.
    pattern = re.compile(r'^(\d{4})_'
                         r'([^_]+)_'
                         r'(\d+g)\.csv$')

    for file in path.iterdir():
        if file.is_file():
            match = pattern.match(file.name)
            if match:
                year, size, freq = match.groups()
                result[(year, size, freq)] = file

    return result

res = group_measurement_files_by_key(Path("../data/measurements"))
print(res)