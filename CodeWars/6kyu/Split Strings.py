def solution(s):
    a = []
    for index, elem in enumerate(s):
        if len(s)-1 == index and len(s) % 2 == 1:
            a.append("{}_".format(s[index]))
        elif index % 2 == 0 and index != len(s)-1:
            a.append("{}{}".format(s[index],s[index+1]))
        else:
            pass
    return a