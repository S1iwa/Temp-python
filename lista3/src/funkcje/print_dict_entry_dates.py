def print_dict_entry_dates(log_dict):
    for uid, entries in log_dict.items():
        ips = set()
        hosts = set()
        methods = {}
        total = len(entries)
        success = 0

        times = []

        for e in entries:
            ips.add(e["ip_orig"])
            hosts.add(e["host"])
            times.append(e["ts"])

            m = e["method"]
            methods[m] = methods.get(m, 0) + 1

            if 200 <= e["status"] < 300:
                success += 1

        print("UID:", uid)
        print("IP:", ips)
        print("HOSTY:", hosts)
        print("Liczba żądań:", total)
        print("Pierwsze:", min(times))
        print("Ostatnie:", max(times))

        print("Metody %:")
        for m, count in methods.items():
            print(m, round(count / total * 100, 2), "%")

        print("2xx ratio:", success / total if total else 0)
        print("-----")