def longest(a1, a2):
    z = sorted(set(list(a1) + list(a2)))
    return ''.join(z)