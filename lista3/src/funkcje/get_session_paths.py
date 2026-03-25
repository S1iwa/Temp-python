def get_session_paths(log):
    result = {}

    for entry in log:
        uid = entry[1]
        uri = entry[8]

        if uid not in result:
            result[uid] = []

        result[uid].append(uri)

    return result