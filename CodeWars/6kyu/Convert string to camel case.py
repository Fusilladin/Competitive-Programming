def to_camel_case(txt):
    txt = txt.replace('-',' ').replace('_',' ')
    #txt = list(txt.split())
    a = []
    if txt == []:
        pass
    else:
        for index, i in enumerate(txt.split()):
#txt.capitalize()
          
            if index == 0:
                    a.append(i)
            else:
                i = i.capitalize()
                a.append(i)
        return ''.join(a)