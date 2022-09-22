def make_readable(sec):
    _min,sec = divmod(sec,60)
    hour,_min = divmod(_min,60)
    #a = [0,0,':',0,0,':',0,0]
    a = ''
    
    if hour > 9:
        a += str(hour) + ':'
    elif hour > 0:
        a += '0' + str(hour) + ':'
    else:
        a += '00:'
    
    if _min > 9:
        a += str(_min) + ':'
    elif _min > 0:
        a += '0' + str(_min) + ':'
    else:
        a += '00:'
    
    if sec > 9:
        a += str(sec)
    elif sec > 0:
        a += '0' + str(sec)
    else:
        a += '00'
    return a
