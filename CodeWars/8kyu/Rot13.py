def rot13(msg):
    a=''
    #print('lower',ord('z'))
    #print('UPPER',ord('Z'))
    for i in msg:
        if i.isupper() == True: 
            o = (ord(i)+13)
            if o > 90:
                o = o-26
                a+=chr(o)
            else:
                a+=chr(o)
        elif i.islower() == True: 
            o = (ord(i)+13)
            if o > 122:
                o = o-26
                a+=chr(o)
            else:
                a+=chr(o)
        else:
            a+=i
    return a
