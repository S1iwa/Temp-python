import sys
from src.funkcje.common import safe_run, get_chars, is_sentence_end

def find_longest_sentence(stream):
    curr_s, longest_s, max_l, last = "", "", 0, ""
    for c in stream:
        curr_s += c
        if is_sentence_end(c, last):
            s_clean = curr_s.strip()
            if len(s_clean) > max_l:
                max_l = len(s_clean)
                longest_s = s_clean
            curr_s = ""
        last = c
    s_clean = curr_s.strip()
    if len(s_clean) > max_l:
        longest_s = s_clean
    return longest_s

def main():
    res = find_longest_sentence(get_chars())
    if res:
        sys.stdout.write(res + "\n")

if __name__ == "__main__":
    safe_run(main())