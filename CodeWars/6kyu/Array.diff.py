def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a