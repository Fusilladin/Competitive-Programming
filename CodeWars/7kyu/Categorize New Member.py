def open_or_senior(data):
    data = list(data)
    a = []
    for i,j in data:
        if i >= 55 and j > 7:
            a.append('Senior')
        else:
            a.append('Open')
    return a
            