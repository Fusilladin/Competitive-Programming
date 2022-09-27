def solution(s):
    #65/90
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            s = s.replace(i,' '+i)
    s = s.replace('  ',' ')
    return s
    