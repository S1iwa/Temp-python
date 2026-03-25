def get_entries_by_code(log, code):
    if not isinstance(log, list) or not isinstance(code, int):
        print("'log' has to be a list, 'code' has to be an integer.")
        return []

    if not log:
        return []

    try:
        return [tup for tup in log if tup[5] == code]
    except IndexError:
        print("Index out of range")
        return []