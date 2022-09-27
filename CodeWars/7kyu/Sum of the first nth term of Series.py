def series_sum(n):
    a = 1
    b = 1
    if n == 1:
        return '1.00'
    elif n == 0:
        return '0.00'
    else:
        for i in range(1,n):
            b += 3
            a += (1/b)
    a = (str(round(a,2)))
    return a.ljust(4,'0')

--

def series_sum(n):
    a = 0
    for i in range(n):
        a+=1/(i*3+1)
    return '{:.2f}'.format(a)