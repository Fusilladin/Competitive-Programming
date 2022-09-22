def increment_string(wrd):
    stripped = wrd.rstrip('1234567890')
    ints = wrd[len(stripped):]
    if len(ints) == 0:
        return wrd+'1'
    else:
        length = len(ints)
        new_ints = int(ints) + 1
        new_ints = str(new_ints).zfill(length)
        return stripped + new_ints

#

def increment_string(wrd):
    stripped = wrd.rstrip('1234567890')
    num = wrd[len(stripped):]
    if len(num) == 0:
        return stripped +'1'
    else:
        length = len(num)
        new_num = int(num)+1
        new_num = str(new_num).zfill(len(num))
        return stripped +new_num