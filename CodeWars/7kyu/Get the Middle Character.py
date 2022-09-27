def get_middle(s):
    x = len(s)
    if x == 1:
        return s
    elif x % 2 == 0:
        return s[x//2-1]+s[x//2]
    else:
        return s[x//2]