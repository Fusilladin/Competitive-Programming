def filter_list(lst):
    print(lst)
    ls = []
    for i in lst:
        if type(i) == int:
            ls.append(i)
        else:
            pass
    
    return ls