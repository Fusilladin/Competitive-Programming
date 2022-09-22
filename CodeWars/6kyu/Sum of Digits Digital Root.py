def digital_root(n):
    while len(str(n)) > 0:
        n = [int(i) for i in str(n)]
        n = sum(n)
        if len(str(n)) == 1:
            break
    return n