def duplicate_encode(word):
    word = word.lower()
    arr = []
    dupe = []
    for i in word:
        if i in dupe:
            pass
        elif i in arr:
            dupe.append(i)
            arr.remove(i)
        else:
            arr.append(i)
            
    res = []
    for i in word:
        if i in arr:
             res.append("(".strip("\n"))
        elif i in dupe:
             res.append(")".strip("\n"))
        else:
            pass
        
    resi = ""
    for elem in res:
        resi += elem
    return resi