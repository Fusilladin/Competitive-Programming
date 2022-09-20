def sum_no_duplicates(l):
    arr = []
    dupe = []
    for i in l:
        if i in dupe:
            pass
        elif i not in arr:
            arr.append(i)
        else:
            arr.remove(i)
            dupe.append(i)
    # print(arr,dupe)
    print(arr,dupe,l)
    return sum(arr)