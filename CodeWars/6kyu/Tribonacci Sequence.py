def tribonacci(sig, n):
    a,b,c = sig
    count = 0
    arr = [a,b,c]
    for i in range(n):
        if count < n:
            d = a+b+c
            a = b
            b = c
            c = d
            arr.append(d)
        else:
            break
    return arr[0:n]