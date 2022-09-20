def sq(arr):
    a = []
    for i in arr:
        x = i ** 0.5
        if type(x) is int:
            a.append(x)
        else:
            a.append(i*i)
    return a
sq([4,3,2,9,49,13])
print(a)