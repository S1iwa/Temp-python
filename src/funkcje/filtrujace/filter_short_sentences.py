import sys
from src.funkcje.common import get_chars, is_sentence_end

def filter_short_sentences(stream):
    curr_s, word_count, in_word, last_c = "", 0, False, ""
    for c in stream:
        curr_s += c
        if c.isalpha():
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False
        if is_sentence_end(c, last_c):
            if 0 < word_count <= 4:
                yield curr_s.strip()
            curr_s, word_count, in_word = "", 0, False
        last_c = c

if __name__ == "__main__":
    for s in filter_short_sentences(get_chars()):
        sys.stdout.write(s + "\n")