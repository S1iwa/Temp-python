from lista3.src.funkcje.entry_to_dict import entry_to_dict

def log_to_dict(log):
    result = {}

    for entry in log:
        uid = entry[1]
        entry_dict = entry_to_dict(entry)

        if uid not in result:
            result[uid] = []

        result[uid].append(entry_dict)

    return result