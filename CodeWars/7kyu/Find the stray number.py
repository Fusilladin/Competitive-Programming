def stray(arr):
    if len(set(arr)) == 2:
        for i in set(arr):
            if arr.count(i) == 1:
                return i
    
    
    
    
    