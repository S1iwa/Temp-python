import sys
import os
import json
import subprocess
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Użycie: py lista4/src/fileAnalizer.py <ścieżka_do_katalogu>")
        return

    directory = sys.argv[1]
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)

                try:
                    process = subprocess.run(
                        ['java', '-cp', 'lista4/src', 'FileReader'],
                        input=filepath,
                        text=True,
                        capture_output=True,
                        check=True
                    )

                    output = process.stdout.strip()
                    if output:
                        data = json.loads(output)
                        if "error" not in data:
                            results.append(data)

                except subprocess.CalledProcessError as e:
                    print(f"Błąd uruchamiania dla {filepath}: {e}")
                except json.JSONDecodeError:
                    print(f"Błąd parsowania JSON dla {filepath}. Zwrócono: {output}")

    total_files = len(results)
    total_chars = sum(r.get('total_characters', 0) for r in results)
    total_words = sum(r.get('total_words', 0) for r in results)
    total_lines = sum(r.get('total_lines', 0) for r in results)

    char_counter = Counter(r.get('most_frequent_character', '') for r in results if r.get('most_frequent_character'))
    word_counter = Counter(r.get('most_frequent_word', '') for r in results if r.get('most_frequent_word'))

    most_freq_char = char_counter.most_common(1)[0][0] if char_counter else ""
    most_freq_word = word_counter.most_common(1)[0][0] if word_counter else ""

    print("--- PODSUMOWANIE STATYSTYK ---")
    print(f"Liczba przeczytanych plików: {total_files}")
    print(f"Sumaryczna liczba znaków: {total_chars}")
    print(f"Sumaryczna liczba słów: {total_words}")
    print(f"Sumaryczna liczba wierszy: {total_lines}")
    print(f"Znak występujący najczęściej (statystycznie): {most_freq_char}")
    print(f"Słowo występujące najczęściej (statystycznie): {most_freq_word}")


if __name__ == "__main__":
    main()
