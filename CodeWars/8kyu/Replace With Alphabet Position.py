def alphabet_position(txt):
    print(txt)
    print(ord('A'))
    a=''
    for i in txt:
        if i.isalpha() == True:
            if i.lower() == i:
                a += str(ord(i)-96)+' '
            else:
                a += str(ord(i)-64)+' '
        else:
            return ''
    return a.rstrip(' ')