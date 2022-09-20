def is_triangle(a, b, c):
    if a+b <= c:
        return False
    elif b+c <= a:
        return False
    elif c+a <= b:
        return False
    else:
        return True
