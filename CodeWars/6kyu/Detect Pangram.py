def is_pangram(s):
    s = s.lower()
    s = set(s)
    a = []
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122 :
            a.append(i)
        else:
            pass
    a = sorted(a)
    a = ''.join(map(str, a))
    if a == 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False
            