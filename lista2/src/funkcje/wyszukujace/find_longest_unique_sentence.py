import sys
from lista2.src.funkcje.common import safe_run, get_chars, is_sentence_end

def find_unique_sentence(stream):
    longest_s, max_l, curr_s = "", 0, ""
    is_valid, last_first_c, in_word, last_c = True, "", False, ""
    for c in stream:
        curr_s += c
        if c.isalpha():
            if not in_word:
                fc = c.lower()
                if fc == last_first_c:
                    is_valid = False
                last_first_c = fc
                in_word = True
        else:
            in_word = False
        if is_sentence_end(c, last_c):
            s_clean = curr_s.strip()
            if is_valid and len(s_clean) > max_l:
                max_l = len(s_clean)
                longest_s = s_clean
            curr_s, is_valid, last_first_c, in_word = "", True, "", False
        last_c = c
    return longest_s

def main():
    res = find_unique_sentence(get_chars())
    if res:
        sys.stdout.write(res + "\n")

if __name__ == "__main__":
    safe_run(main)