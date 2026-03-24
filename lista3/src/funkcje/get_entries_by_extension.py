def get_entries_by_extension(log, ext):
    if not isinstance(log, list) or not isinstance(ext, str):
        return []

    target_ext = f".{ext}"

    try:
        return [
            tup for tup in log
            if tup[9].split('?')[0].endswith(target_ext)
        ]
    except (IndexError, TypeError):
        return []