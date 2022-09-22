def find_it(seq):
    for i in seq:
        x = seq.count(i)
        if x % 2 != 0:
            return i
        else:
            pass
    