def sort_array(arr):
    b = []
    c = []
    for i in arr:
        if i % 2 == 1:
            b.append(i)
    b = sorted(b)
    count = 0
    for i in arr:
        if i % 2 == 0:
            c.append(i)
        elif i % 2 == 1:
            c.append(b[count])
            count +=1
    return c
        
            
    