def entry_to_dict(entry):
    return {
        "ts": entry[0],
        "uid": entry[1],
        "ip_orig": entry[2],
        "port_orig": entry[3],
        "ip_resp": entry[4],
        "port_resp": entry[5],
        "method": entry[6],
        "host": entry[7],
        "uri": entry[8],
        "status": entry[9]
    }