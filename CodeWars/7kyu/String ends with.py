def solution(string, ending):
    print(string,ending)
    if string == ending:
        return True
    elif len(string) == 0 or len(ending) == 0:
        return True
    else:
        ln = len(ending)
        print(ln)
        st = string[:0:-1]
        print(st[ln-1::-1])
        if ending == st[ln-1::-1]:
            return True
        else:
            return False