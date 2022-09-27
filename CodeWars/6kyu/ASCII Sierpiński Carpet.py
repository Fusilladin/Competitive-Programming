# Draw a Sierpiński carpet ^^
def sierpinski_carpet_string(n):
    c0 = '  '
    c1 = ['██']
    while n:
        t = []
        for c in c1:
            t.append(c*3)
        for c in c1:
            t.append(c + c0 + c)
        for c in c1:
            t.append(c*3)
        c1=t
        c0*=3
        n-=1
    return '\n'.join(c1)