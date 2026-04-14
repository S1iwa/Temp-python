import os
import csv
from datetime import datetime

def get_output_dir():
    """Pobiera ścieżkę z CONVERTED_DIR lub ustawia domyślną 'converted/'"""
    default_dir = os.path.join(os.getcwd(), 'converted')
    output_dir = os.environ.get('CONVERTED_DIR', default_dir)

    # Czy katalog istnieje
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def generate_output_filename(original_filename, target_format):
    """Tworzy nazwę pliku z timestampem, np. 20250324-video123.webm"""
    timestamp = datetime.now().strftime("%Y%m%d")
    base_name = os.path.splitext(original_filename)[0]
    # Usuwamy ewentualną kropkę z formatu, jeśli użytkownik podał np. '.mp4'
    target_format = target_format.lstrip('.')
    return f"{timestamp}-{base_name}.{target_format}"


def log_conversion_history(output_dir, original_path, target_format, output_path, tool_used):
    """Zapisuje historię konwersji do pliku history.csv"""
    history_file = os.path.join(output_dir, 'history.csv')
    file_exists = os.path.isfile(history_file)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(history_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                ['Data i godzina', 'Sciezka oryginalnego pliku', 'Format wyjsciowy', 'Sciezka pliku wynikowego',
                 'Uzyty program'])

        writer.writerow([current_time, original_path, target_format, output_path, tool_used])