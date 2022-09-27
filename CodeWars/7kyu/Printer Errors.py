def printer_error(s):
    print(s)
    print(ord('m'))
    count=0
    for i in list(s):
        if ord(i) > 109:
            count+=1
    return '{}/{}'.format(count,len(s))