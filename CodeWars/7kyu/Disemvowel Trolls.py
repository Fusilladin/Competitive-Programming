def disemvowel(let):
    vowels = {'a','e','i','o','u'}
    a = []
    for i in (let):
        if i.lower() not in vowels:
            a.append(i)
    a = ''.join(a)
    return a