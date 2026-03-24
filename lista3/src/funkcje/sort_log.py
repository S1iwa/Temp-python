def sort_log(log, index):
    if not log:
        return []

    try:
        return sorted(log, key=lambda tup: tup[index])
    except IndexError:
        print("Index out of range")
        return []
    except TypeError:
        print("Wrong input")
        return []