def sum_string(s):
    sm = 0
    for digit in s:
        sm += int(digit)
    return sm

def order_weight(lst):
    ls = sorted(lst.split())
    result = " ".join(sorted(ls,key=sum_string))
    return result