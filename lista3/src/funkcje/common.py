def is_dot_decimal(num):
    parts = str(num).split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            if not int(part) >= 0 and int(part) <= 255:
                return False

    return True