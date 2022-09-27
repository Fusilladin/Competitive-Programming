def find_uniq(arr):
    def low(a):
        return set(arr[a].lower())
    
    if low(0) == low(1):
        maj = low(0)
    elif low(0) == low(2):
        maj = low(0)
    else:
        maj = low(1)
    
    for string in arr:
        if set(string.lower()) != maj:
            return string
        