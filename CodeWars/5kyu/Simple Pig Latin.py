def pig_it(txt):
    a = []
    for i in txt.split():
        if i.isalpha():
            a.append(i[1:]+i[0]+'ay')
        else:
            a.append(i)
    return ' '.join(a)

#

def pig_it(txt):
    a = []
    for i in txt.split():
        if i.isalpha():
            a.append(i[1:]+i[0]+'ay')
        else:
            a.append(i)
    return ' '.join(a)