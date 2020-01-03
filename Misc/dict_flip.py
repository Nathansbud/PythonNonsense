def flip(d):
    flipped = {}
    for elem in d:
        if d[elem] not in flipped: flipped[d[elem]] = [elem]
        else: flipped[d[elem]].append(elem)
    return flipped

print(flip({"a":"b", "b":"b", 1:"b", 2:"b"}))