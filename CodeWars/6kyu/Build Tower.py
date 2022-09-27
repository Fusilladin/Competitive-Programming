def tower_builder(n):
    if n == 0:
        return []
    count = 1
    result = []
    for i in range(1,n+1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n-i)
        result.append(space + stars + space)
        
    return result
