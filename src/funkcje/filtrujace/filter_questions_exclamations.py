import sys
from src.funkcje.common import get_chars, is_sentence_end

def filter_questions_and_exclamations(stream):
    curr_s, last_c = "", ""
    for c in stream:
        curr_s += c
        if is_sentence_end(c, last_c):
            if c == '?' or c == '!':
                yield curr_s.strip()
            curr_s = ""
        last_c = c

if __name__ == "__main__":
    for s in filter_questions_and_exclamations(get_chars()):
        sys.stdout.write(s + "\n")