def find_outlier(num):
    e = []
    o = []
    for i in num:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    if len(e) == 1:
        return int(str(e).strip('[]'))
    else:
        return int(str(o).strip('[]'))
    #
    
    def find_outlier(num):
    e = []
    o = []
    for i in num:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    if len(e) == 1:
        return e[0]
    else:
        return o[0]