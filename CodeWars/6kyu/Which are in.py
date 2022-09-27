def in_array(a1, a2):
    a = []
    for i in sorted(set(a1)):
        for j in sorted(set(a2)):
            if i in j:
                a.append(i)
                break
    return a 