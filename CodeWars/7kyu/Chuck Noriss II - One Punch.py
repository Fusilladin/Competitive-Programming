def one_punch(item): 
    if type(item) == int:
        return 'Broken!'
    elif item == '':
        return 'Broken!'
    elif type(item) == str:   
        item = item.split()
        item.sort()
        item = ' '.join(item)
        item = item.replace("e",'').replace("E",'').replace("a",'').replace("A",'')
        return item
    else: return 'Broken!'
    