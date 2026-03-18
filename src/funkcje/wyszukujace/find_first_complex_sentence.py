import sys
from src.funkcje.common import get_chars, is_sentence_end

def find_first_complex_sentence(stream):
    curr_s, commas, last_c = "", 0, ""
    for c in stream:
        curr_s += c
        if c == ',':
            commas += 1
        if is_sentence_end(c, last_c):
            if commas > 1:
                return curr_s.strip()
            curr_s, commas = "", 0
        last_c = c
    return ""

if __name__ == "__main__":
    res = find_first_complex_sentence(get_chars())
    if res:
        sys.stdout.write(res + "\n")