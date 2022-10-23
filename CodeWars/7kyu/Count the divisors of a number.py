def divisors(n):
    a = []
    print(n)
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
            print(i)
    return len(a)