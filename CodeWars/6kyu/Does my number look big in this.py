def narcissistic(val):
    ln = len(str(val))
    if ln == 1:
        return True
    num = 0
    for i in str(val):
        num += (int(i)**ln)
    if num == val:
        return True
    else:
        return False