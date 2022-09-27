def remove_smallest(num):
    nm = []
    for i in num:
        nm.append(i)
    a = -1
    for i in set(nm):
        if a < 0 or i < a:
            a = i
    for i in nm:
        print(i,a)
        if i == a:
            nm.remove(a)
            break
    return nm
