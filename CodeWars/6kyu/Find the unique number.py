def find_uniq(arr):
    lst = set(arr)
    for i in lst:
        if arr.count(i) == 1:
            return i
        else:
            pass