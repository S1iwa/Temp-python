def count_by_method(log):
    if not isinstance(log, list):
        return {}

    counts = {}
    try:
        for tup in log:
            method = tup[7]
            counts[method] = counts.get(method, 0) + 1
        return counts
    except IndexError:
        return {}