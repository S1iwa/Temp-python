from lista3.src.funkcje.common import is_dot_decimal


def get_top_ips(log, n=10):
    ips = []
    counters = []
    for tup in log:
        ips.append(tup[2])
        is_dot_decimal(tup[4])