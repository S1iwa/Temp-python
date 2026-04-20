import os
import json
from pathlib import Path


def get_converted_dir():
    return os.environ.get('CONVERTED_DIR', os.path.join(os.getcwd(), 'converted'))


def find_media_files(directory):
    audio_video_ext = {'.mp4', '.avi', '.mkv', '.mp3', '.wav', '.webm'}
    image_ext = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

    found_files = []
    for root, _, filenames in os.walk(directory):
        for f in filenames:
            ext = Path(f).suffix.lower()
            filepath = os.path.join(root, f)
            if ext in audio_video_ext:
                found_files.append((filepath, 'audio_video'))
            elif ext in image_ext:
                found_files.append((filepath, 'image'))
    return found_files


def log_history(target_dir, record):
    history_file = os.path.join(target_dir, 'history.json')
    history = []

    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                pass

    history.append(record)

    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)