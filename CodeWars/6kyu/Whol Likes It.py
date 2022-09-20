def likes(names):
    if names == []:
        return "no one likes this"
    else:
        pass
    x = len(names)
    if x == 1:
        return "{} likes this".format(names[0])
    elif x == 2:
        return "{} and {} like this".format(names[0],names[1])
    elif x == 3:
        return "{}, {} and {} like this".format(names[0],names[1],names[2])
    else:
        return "{}, {} and {} others like this".format(names[0],names[1],x-2)