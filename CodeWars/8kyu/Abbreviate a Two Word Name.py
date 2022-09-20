def abbrev_name(name):
    first,last = name.upper().split(' ')
    return '{}.{}'.format(first[0],last[0])