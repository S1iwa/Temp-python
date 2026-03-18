import sys


def clean_line(line):
    # usuwa whitespace na brzegach i dodatkowe spacje
    return " ".join(line.strip().split())

def is_empty(line):
    return line.strip() == ""

def read():
    sys.stdin.reconfigure(encoding='utf-8') #encoding
    lines = sys.stdin.readlines()

    result = ""
    # znalezienie preambuły
    start_index = 0
    empty_count = 0

    for i in range(min(10, len(lines))):
        if is_empty(lines[i]):
            empty_count += 1
            if empty_count == 2:
                start_index = i + 1
                break
        else:
            empty_count = 0
    content = lines[start_index:]

    for line in content:
        stripped = line.strip()

        # koniec tekstu
        if stripped == "-----":
            break

        if is_empty(line):
            result += "\n"
        else:
            result += clean_line(line) + "\n"
    return result

if __name__ == "__main__":
    print(read())

