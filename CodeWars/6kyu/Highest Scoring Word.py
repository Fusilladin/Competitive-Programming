def high(x):
    b = 0
    for i in x.split():
        i = i
        a = 0
        for j in i:
            a+=(ord(j)-96)
        if a > b:
            b = a
    for i in x.split():
        a = 0
        for j in i:
            a+=(ord(j)-96)  
        if a == b:
            return i
            
            
    