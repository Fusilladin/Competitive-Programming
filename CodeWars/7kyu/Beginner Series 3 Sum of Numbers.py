def get_sum(a,b):
    print(a,b)
    z = 0
    if a < b:
        x = range(a,b+1)
        for n in x:
            z+=n     
            #print(n)
    elif b < a:
        x = range(b,a+1)
        for n in x:
            z+=n
            #print(n)
    else:
        return a
    '''
    z = 0
    for i in str(n):
        print(i)
        z += int(i)
    print(z,'end')
    '''
    return z
    

    