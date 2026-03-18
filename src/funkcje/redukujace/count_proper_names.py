import sys
from src.funkcje.common import safe_run, get_chars, is_sentence_end, is_proper_name

def get_percentage(stream):
    total_s, with_p = 0, 0
    word_idx, in_word, has_p, last = 0, False, False, ""
    for c in stream:
        if is_sentence_end(c, last):
            if word_idx > 0:
                total_s += 1
                with_p += has_p
            word_idx, has_p, in_word = 0, False, False
        elif c.isalpha():
            if not in_word:
                in_word = True
                word_idx += 1
                if is_proper_name(c, word_idx):
                    has_p = True
        else:
            in_word = False
        last = c
    if word_idx > 0:
        total_s += 1
        with_p += has_p
    return (with_p / total_s * 100) if total_s > 0 else 0

def main():
    sys.stdout.write(format(get_percentage(get_chars()), ".2f") + "%\n")

if __name__ == "__main__":
    safe_run(main())