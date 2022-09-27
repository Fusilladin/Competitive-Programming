def duplicate_count(txt):
    print(txt)
    cnt = 0
    text = txt.lower()
    for i in set(text):
        alpha = i.isalpha()
        if alpha is True:
            print(i)
            
            #print('pass')
            n = txt.lower().count(i)
            if n > 1:
                print(n)
                cnt+=1
        else:
            print(i)
            n = txt.count(i)
            if n > 1:
                cnt+=1
    return cnt