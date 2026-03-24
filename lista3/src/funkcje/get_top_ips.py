from lista3.src.funkcje.common import is_dot_decimal

def get_top_ips(log, n=10):
    if not isinstance(log, list) or not isinstance(n, int):
        return []

    counts = {}
    try:
        for tup in log:
            ip_orig = tup[2]
            ip_resp = tup[4]

            if is_dot_decimal(ip_orig):
                counts[ip_orig] = counts.get(ip_orig, 0) + 1

            if is_dot_decimal(ip_resp):
                counts[ip_resp] = counts.get(ip_resp, 0) + 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_counts[:n]
    except IndexError:
        return []