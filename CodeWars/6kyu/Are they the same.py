def comp(a1, a2):
    if a1 == [] and a2 ==[]:
        return True
    elif a1 == [] or a2 == []:
        return False
    elif len(a1) != len(a2):
        return False
    else:
        for i in set(a1):
            if i**2 in a2:
                pass
            else:
                return False
    for i in set(a1):
        if a1.count(i) > 1:
            if a2.count(i**2) == a1.count(i):
                pass
            else:
                return False
    return True

--

def comp(a1, a2):
    try:
        a1 = sorted(i**2 for i in a1)
        a2 = sorted(a2)
        return a1 == a2
    except:
        return False