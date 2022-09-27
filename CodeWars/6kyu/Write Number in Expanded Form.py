def expanded_form(num):
    count = 0
    a = []
    for i in str(num):
        a.append(i)
    k = []
    for j in a:
        zeros = len(a) - count
        j = j.ljust(zeros,'0')
        count +=1
        if int(j) != 0:
            k.append(j)
        else:
            pass
    k = ' + '.join(k)
    return k