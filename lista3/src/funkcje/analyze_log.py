from lista3.src.funkcje.get_top_uris import get_top_uris


def analyze_log(log):
    ip_counts = {}
    method_counts = {}
    error_count = 0

    for entry in log:
        ip = entry[2]
        method = entry[6]
        status = entry[9]

        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        method_counts[method] = method_counts.get(method, 0) + 1

        if status >= 400:
            error_count += 1

    top_ip = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_uri = get_top_uris(log, 5)

    return {
        "top_ip": top_ip,
        "top_uri": top_uri,
        "methods": method_counts,
        "errors": error_count,
        "total_requests": len(log)
    }