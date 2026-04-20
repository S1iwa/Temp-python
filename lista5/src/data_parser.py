import csv
import os


def parse_data(dir_path):
    result = {
        "stacje": {},
        "pomiary": {}
    }

    # --- parsowanie stacji ---
    stacje_path = os.path.join(dir_path, "stacje.csv")

    with open(stacje_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kod = row["Kod stacji"]
            result["stacje"][kod] = row

    # --- parsowanie pomiarów ---
    measurements_path = os.path.join(dir_path, "measurements")

    for file_name in os.listdir(measurements_path):
        if file_name.endswith(".csv"):

            full_path = os.path.join(measurements_path, file_name)

            with open(full_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)

                data = []
                for row in reader:
                    data.append(row)

                result["pomiary"][file_name] = data

    return result
data = parse_data("../data")

# przykład:
print(data["stacje"]["DsBialka"])
print(data["pomiary"]["2023_PM10_24g.csv"][:3])