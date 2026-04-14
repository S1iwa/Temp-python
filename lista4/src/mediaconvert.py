import sys
import os
import argparse
import subprocess
import utils

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'}
MEDIA_EXTENSIONS = {'.mp4', '.avi', '.mkv', '.webm', '.mp3', '.wav', '.ogg', '.flac', '.mov'}

def determine_tool(filename):
    """Decyduje, czy użyć ffmpeg czy magick na podstawie rozszerzenia"""
    ext = os.path.splitext(filename)[1].lower()
    if ext in IMAGE_EXTENSIONS:
        return 'magick'
    elif ext in MEDIA_EXTENSIONS:
        return 'ffmpeg'
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description="Skrypt do konwersji plików audio/wideo oraz obrazów.")
    parser.add_argument("input_dir", help="Ścieżka do katalogu z plikami wejściowymi")
    parser.add_argument("target_format", help="Format wyjściowy (np. mp4, webm, png)")

    args = parser.parse_args()
    input_dir = args.input_dir
    target_format = args.target_format

    if not os.path.isdir(input_dir):
        print(f"Błąd: Katalog wejściowy '{input_dir}' nie istnieje")
        sys.exit(1)

    output_dir = utils.get_output_dir()
    print(f"Katalog docelowy: {output_dir}")

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        if not os.path.isfile(input_path):
            continue

        tool = determine_tool(filename)
        if not tool:
            print(f"Pominięto plik {filename} (nieobsługiwane rozszerzenie).")
            continue

        output_filename = utils.generate_output_filename(filename, target_format)
        output_path = os.path.join(output_dir, output_filename)

        print(f"Konwertowanie: {filename} -> {output_filename} (przy użyciu {tool})...")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(base_dir)

        if tool == 'ffmpeg':
            exe_path = os.path.join(parent_dir, 'bin', 'ffmpeg.exe')
            cmd = [exe_path, '-y', '-i', input_path, '-loglevel', 'error', output_path]
        elif tool == 'magick':
            exe_path = os.path.join(parent_dir, 'bin', 'ImageMagick', 'magick.exe')
            cmd = [exe_path, input_path, output_path]

        if not os.path.exists(exe_path):
            print(f"Błąd krytyczny: Nie znaleziono lokalnego programu w {exe_path}!")
            print("Pobierz go i daj do folderu 'bin' w swoim projekcie")
            sys.exit(1)

        try:
            subprocess.run(cmd, check=True)

            utils.log_conversion_history(output_dir, input_path, target_format, output_path, tool)
            print("Sukces!")

        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas konwersji pliku {filename}. Szczegóły: {e}")


if __name__ == "__main__":
    main()