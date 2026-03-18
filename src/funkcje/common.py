import sys

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