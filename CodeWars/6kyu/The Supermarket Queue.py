def queue_time(cus, n):
    qu = [0]*n
    for i in cus:
        qu = sorted(qu)
        qu[0] += i
    return max(qu)