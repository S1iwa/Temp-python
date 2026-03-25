def get_top_uris(log, n=10):
    counts = {}

    # liczenie wystąpień
    for tup in log:
        uri = tup[8]
        if uri in counts:
            counts[uri] += 1
        else:
            counts[uri] = 1

    # zamiana na listę i sortowanie malejąco po liczbie wystąpień
    sorted_uris = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_uris[:n] #zwracanie 10 pierwszych