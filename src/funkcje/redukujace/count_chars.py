import sys
from src.funkcje.common import get_chars

def count_chars(stream):
    n = 0
    for c in stream:
        if not c.isspace():
            n += 1
    return n

if __name__ == "__main__":
    sys.stdout.write(str(count_chars(get_chars())) + "\n")