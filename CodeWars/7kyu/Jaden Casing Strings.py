def to_jaden_case(string):
    string = string.split()
    a = ''
    for i in string:
        a += str(i).capitalize()+' '
    return a.rstrip()