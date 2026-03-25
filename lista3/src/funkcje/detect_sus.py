def detect_sus(log, threshold, time_window=1):
    ip_data = {}

    for entry in log:
        ip = entry[2]
        ts = entry[0].timestamp()
        status = entry[9]

        if ip not in ip_data:
            ip_data[ip] = {
                "count": 0,
                "errors_404": 0,
                "times": []
            }

        ip_data[ip]["count"] += 1
        ip_data[ip]["times"].append(ts)

        if status == 404:
            ip_data[ip]["errors_404"] += 1

    suspicious = []

    for ip, data in ip_data.items():
        fast_requests = 0
        times = sorted(data["times"])

        # sprawdzanie krótkich odstępów
        for i in range(1, len(times)):
            if times[i] - times[i-1] < time_window:
                fast_requests += 1

        # warunki podejrzane
        if (
            data["count"] > threshold or
            data["errors_404"] > threshold // 2 or
            fast_requests > threshold // 2
        ):
            suspicious.append(ip)

    return suspicious