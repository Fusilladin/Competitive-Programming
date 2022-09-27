def reverse_words(txt):
    print(txt,'txt\n')
    a=''
    for i in txt.split(' '):
        a+=(i[::-1]+' ')
    print(a,'answer')
    return a.rstrip()