def count_bits(n):
    n = list(bin(n))
    n = n[2:]
    x = 0
    for i in n:
        if i == '1':
            x += 1
        else:
            pass
    return x