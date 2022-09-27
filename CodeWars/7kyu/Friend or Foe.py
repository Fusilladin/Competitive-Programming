def friend(x):
    a = ''
    for i in x:
        if len(i) == 4:
            a += i+' '
        else:
            pass
    return list(a.split())