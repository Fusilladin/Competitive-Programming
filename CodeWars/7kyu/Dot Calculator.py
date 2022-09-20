def calculator(txt):
    x,y,z = txt.split(' ')
    a = len(x)
    c = len(z)
    t = eval("{}{}{}".format(a,y,c))
    #print(t)

    count = 0
    dots = []
    while count < t:
        count+=1
        dots.append('.')
    _str = ''
    answer = (_str.join(dots))
    if t == 0:
        return ''
    else:
        return answer
