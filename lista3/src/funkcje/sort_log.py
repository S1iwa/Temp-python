def sort_log(log, index):
    if not isinstance(index, int):
        return []

    try:
        return sorted(log, key=lambda tup: tup[index])
    except IndexError:
        print("Index out of range")
        return []