import sys
from lista2.src.funkcje.common import safe_run, get_chars, is_sentence_end

def filter_questions_and_exclamations(stream):
    curr_s, last_c = "", ""
    for c in stream:
        curr_s += c
        if is_sentence_end(c, last_c):
            if c == '?' or c == '!':
                yield curr_s.strip()
            curr_s = ""
        last_c = c

def main():
    for s in filter_questions_and_exclamations(get_chars()):
        sys.stdout.write(s + "\n")

if __name__ == "__main__":
    safe_run(main)