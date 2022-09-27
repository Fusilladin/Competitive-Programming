def number(lines):
    a = []
    for index, strng in enumerate(lines,start=1):
        a.append("{}: {}".format(index,strng))
    return a