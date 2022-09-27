x = input()
a = []
for i in set(x):
    if i.isalpha is True:
        a.append(i)
    else:
        pass
for i in x:
    if type(i) == int:
        print((next(i)))
        pass
    
