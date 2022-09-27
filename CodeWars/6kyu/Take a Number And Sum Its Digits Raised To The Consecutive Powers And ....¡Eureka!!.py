def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    arr = []
    for i in range(a,b+1):
        power = 0
        for index,j in enumerate(str(i),1):
            power += (int(j)**index)
        if power == i:
            arr.append(power)
        else:
            pass
    return arr