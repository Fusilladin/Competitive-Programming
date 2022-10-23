def dont_give_me_five(start,end):
    print(start,end)
    count = 0
    for i in range(start,end+1):
        if '5' in str(i):
            print(i)
        else:
            count += 1
    return count