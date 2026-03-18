import sys
from src.funkcje.common import get_chars, is_sentence_end

def filter_first_sentences(stream, number=20):
    curr_s, last_c, count = "", "", 0
    for c in stream:
        curr_s += c
        if is_sentence_end(c, last_c):
            s_clean = curr_s.strip()
            if s_clean:
                yield s_clean
                count += 1
                if count >= number:
                    break
            curr_s = ""
        last_c = c

if __name__ == "__main__":
    for s in filter_first_sentences(get_chars()):
        sys.stdout.write(s + "\n")