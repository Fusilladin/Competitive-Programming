def descending_order(num):
    num = str(num)
    a = []
    for i in num:
        a.append(i)
    b = []
    while len(a) > 0:
        for i in a:
            if i == max(a):
                b.append(i)
                a.remove(i)
    return int(''.join(b))

    #

    def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)