def get_extension_stats(log):
    result = {}

    for entry in log:
        uri = entry[8]

        if "." in uri:
            ext = uri.split(".")[-1]
            result[ext] = result.get(ext, 0) + 1

    return result