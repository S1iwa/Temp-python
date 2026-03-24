import sys

def safe_run(main_func):
    try:
        return main_func()
    except BrokenPipeError:
        return sys.exit(0)
    except Exception as e:
        sys.stdout.write(str(e))
        sys.exit(1)

def get_chars():
    while char := sys.stdin.read(1):
        yield char

def is_sentence_end(char, last_char):
    return char in ".!?" or (char == '\n' and last_char == '\n')

def is_proper_name(char, word_idx):
    return char.isupper() and word_idx > 1

def is_conjunction(word):
    w = word.lower()
    return w == "i" or w == "oraz" or w == "ale" or w == "że" or w == "lub"