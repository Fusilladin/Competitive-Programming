def divisors(integer):
    a = []
    for i in range(2,integer):
        if integer % i == 0:
            a.append(i)
    if a != []:
        return a
    else:
        return '{} is prime'.format(integer)