def delete_nth(order,e):
    a = []
    for i in order:
        if a.count(i) < e:
            a.append(i)
    return a

--

def delete_nth(order,e):
    a = []
    for i in order:
        if a.count(i) < e:
            a.append(i)
    return a