def count_status_classes(log):
    result = {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}

    for tup in log:
        status = tup[9]

        if 200 <= status < 300:
            result["2xx"] += 1
        elif 300 <= status < 400:
            result["3xx"] += 1
        elif 400 <= status < 500:
            result["4xx"] += 1
        elif 500 <= status < 600:
            result["5xx"] += 1

    return result