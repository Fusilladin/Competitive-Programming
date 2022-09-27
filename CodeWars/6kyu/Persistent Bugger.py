def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        a = 1
        for i in n:
            a *= int(i)
        n = str(a)
        count += 1
    return count