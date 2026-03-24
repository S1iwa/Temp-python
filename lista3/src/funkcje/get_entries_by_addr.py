from lista3.src.funkcje.common import is_dot_decimal

def get_entries_by_addr(log, addr):
    if not isinstance(log, list):
        return []

    # id orig h - 2
    # host - 8

    try:
        if is_dot_decimal(addr):
            return [tup for tup in log if tup[2] == addr]
        else:
            return [tup for tup in log if tup[8] == addr]
    except IndexError:
        print("Index out of range")
        return []