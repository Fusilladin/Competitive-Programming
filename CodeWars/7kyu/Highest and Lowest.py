def high_and_low(num):
    num = num.split(' ')
    a = []
    for i in num:
        if type(int(i)) == int:
            a.append(int(i))
    x,y = (max(a),min(a))
    return '{} {}'.format(x,y)