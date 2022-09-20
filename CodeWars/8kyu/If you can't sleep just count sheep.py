def count_sheep(n):
    # your code
    return ''.join('{} sheep...'.format(i) for i in range(1,n+1))