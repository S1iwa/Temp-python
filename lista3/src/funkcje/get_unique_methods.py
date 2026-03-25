def get_unique_methods(log):
    if not isinstance(log, list):
        return []

    try:
        return list({tup[7] for tup in log})
    except IndexError:
        return []