import sys
from src.funkcje.common import safe_run, get_chars, is_sentence_end, is_conjunction

def filter_conj(stream):
    curr_s, curr_word, last_c = "", "", ""
    matches, in_word = 0, False
    for c in stream:
        curr_s += c
        if c.isalpha():
            curr_word += c
            in_word = True
        else:
            if in_word:
                if is_conjunction(curr_word):
                    matches += 1
                curr_word = ""
            in_word = False
        if is_sentence_end(c, last_c):
            if matches >= 2:
                yield curr_s.strip()
            curr_s, matches = "", 0
        last_c = c

def main():
    for s in filter_conj(get_chars()):
        sys.stdout.write(s + "\n")

if __name__ == "__main__":
    safe_run(main)