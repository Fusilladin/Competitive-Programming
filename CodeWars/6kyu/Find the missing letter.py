def find_missing_letter(chars):
    y = 0
    for i in chars:
        x = (ord(i))
        if y == 0:
            pass
        elif x-1 != y:
            return chr(y+1)
        else: 
            pass
        y = x