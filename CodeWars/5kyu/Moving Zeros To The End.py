def move_zeros(lst):
    o = []
    b = []
    for i in lst:
        if i == 0:
            o.append(i)                
        else:
            b.append(i)
    return b+o

#

def move_zeros(arr):
    l = [i for i in arr if isinstance(i,bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

#

def move_zeros(arr):
    l = [i for i in arr if i!=0]
    return l+[0]*(len(arr)-len(l))

#

def move_zeros(lst):
    a = []
    b = []
    for i in lst:
        if i == 0:
            b.append(i)
        else:
            a.append(i)
    return a+b