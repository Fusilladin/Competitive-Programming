def productFib(n):
        a = 0
        b = 1
        print(n)
        if n < 0:
            pass
            #print('Try again')
        elif n == 0:
            return [0,1,True]
        elif n == 1:
            return [1,1,True]
        elif n == 2:
            return [1,2,True]
        elif n == 3:
            return [2,3,False]
        elif n == 4:
            return [2,3,False]
        else:
            pass
            #print(a)
            #print(b)
        c=0
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            if a*b == n:
                return [a,b,True]
            elif a*b > n:
                return [a,b,False]
            else:
                pass
        print(a,b,'True')