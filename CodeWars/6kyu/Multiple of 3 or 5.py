def solution(num):
    a = []
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            a.append(i)
        else:
            pass
    return sum(a)