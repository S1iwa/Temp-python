import re
from data_parser import parse_data


def zadanie_4(dir_path="../data"):
    dane = parse_data(dir_path)
    stacje = list(dane["stacje"].values())

    # a
    re_data = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
    daty = [re_data.findall(s[k]) for s in stacje for k in ["Data uruchomienia", "Data zamknięcia"] if s.get(k)]

    # b
    re_wspol = re.compile(r"-?\d+\.\d{6}")
    wspolrzedne = [re_wspol.findall(s[k]) for s in stacje for k in ["WGS84 φ N", "WGS84 λ E"] if s.get(k)]

    # c
    re_2czlony = re.compile(r"^[^-]+-[^-]+$")
    dwuczlony = [s["Nazwa stacji"] for s in stacje if re_2czlony.match(s["Nazwa stacji"])]

    # d
    mapa = str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ")
    zmienione_nazwy = [s["Nazwa stacji"].translate(mapa).replace(" ", "_") for s in stacje]

    # e
    stacje_mob = [s for s in stacje if s["Kod stacji"].endswith("MOB")]
    czy_mobilne = all(s["Rodzaj stacji"].lower() == "mobilna" for s in stacje_mob)

    # f
    re_3czlony = re.compile(r"^[^-]+-[^-]+-[^-]+$")
    trzyczlony = [s["Nazwa stacji"] for s in stacje if re_3czlony.match(s["Nazwa stacji"])]

    # g
    re_ulal = re.compile(r",.*\b(?:ul|al)\.", re.IGNORECASE)
    ul_al = [s["Adres"] for s in stacje if s.get("Adres") and re_ulal.search(s["Adres"])]

    return daty, wspolrzedne, dwuczlony, zmienione_nazwy, czy_mobilne, trzyczlony, ul_al


if __name__ == "__main__":
    wyniki = zadanie_4()
    print("Czy stacje MOB są zawsze mobilne?", wyniki[4])
    print("Przykładowe stacje 3-członowe:", wyniki[5][:3])