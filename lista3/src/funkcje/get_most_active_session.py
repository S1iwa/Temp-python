def get_most_active_session(log_dict):
    max_uid = None
    max_count = 0

    for uid, entries in log_dict.items():
        if len(entries) > max_count:
            max_count = len(entries)
            max_uid = uid

    return max_uid