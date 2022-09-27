def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        a = 0
        b = 0
        for i in walk:
            if i == 'n':
                a+= 1
            elif i == 's':
                a-=1
            elif i == 'w':
                b +=1
            elif i == 'e':
                b -=1
            else:
                pass
    if a == 0 and b == 0:
        return True
    else: 
        return False

--

def is_valid_walk(walk):
    if len(walk) == 10:
        if walk.count('e') == walk.count('w') and walk.count('n') == walk.count('s'):
            return True
        else:
            return False
    else:
        return False