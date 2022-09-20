def distinct(seq):
    arr = []
    dupe = []
    for i in seq:
        if i not in arr:
            arr.append(i)
        else:
            dupe.append(i)
    return arr