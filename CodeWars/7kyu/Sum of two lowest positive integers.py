def sum_two_smallest_numbers(num):
    num = set(num)
    a = min(num)
    num.discard(a)
    b = min(num)
    return a+b