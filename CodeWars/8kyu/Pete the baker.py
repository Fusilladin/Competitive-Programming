def cakes(rec, avail):    
    y = 0
    print(rec,'\n')
    print(avail)
    for i in rec:
        if i not in avail:
            return 0
        else:
            x = avail[i] // rec[i]
            if x < y or y == 0:
                y = x
    return y