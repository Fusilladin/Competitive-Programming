def find_short(lst):
    
    lst = lst.split(' ')
    a = 0
    for i in lst:
        x = len(i)
        if x < a or a == 0: 
            a = x
        else:
            pass
    return a
    