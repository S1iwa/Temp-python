def get_failed_reads(log, merge=False):
    if not isinstance(log, list):
        return [] if merge else ([], [])

    try:
        if merge:
            return [tup for tup in log if 400 <= tup[14] < 600]
        return [tup for tup in log if 400 <= tup[14] < 500], [tup for tup in log if 500 <= tup[14] < 600]
    except (IndexError, TypeError):
        return [] if merge else ([], [])