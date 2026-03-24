def is_dot_decimal(num):
    parts = str(num).split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            if not int(part) >= 0 and int(part) <= 255:
                return False

    return True

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