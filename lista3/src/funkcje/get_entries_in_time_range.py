import datetime

def get_entries_in_time_range(log, start, end):
    if not isinstance(log, list):
        return []

    if not isinstance(start, datetime.datetime) or not isinstance(end, datetime.datetime):
        return []

    try:
        return [entry for entry in log if start <= entry[0] < end]
    except (IndexError, TypeError):
        return []