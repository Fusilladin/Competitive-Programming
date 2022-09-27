# return masked string
def maskify(cc):
    x = len(cc)
    y = len(cc[0:x-4])
    if x <= 4:
        return cc
    else:
        return ('#'*y)+'{}'.format(cc[x-4:])