import sys
from src.funkcje.common import safe_run, get_chars

def count_paragraphs(stream):
    count, last, has_content = 0, "", False
    for c in stream:
        if c == '\n' and last == '\n' and has_content:
            count += 1
            has_content = False
        elif not c.isspace():
            has_content = True
        last = c
    return count + (1 if has_content else 0)

def main():
    sys.stdout.write(str(count_paragraphs(get_chars())) + "\n")

if __name__ == "__main__":
    safe_run(main())