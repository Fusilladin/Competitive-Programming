def house_numbers_sum(inp):
    x = 0
    for i in inp:
        if i > 0:
            x += i
        else:
            break
    return x