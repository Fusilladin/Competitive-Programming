def generate_hashtag(s):
    if s == '':
        return False
    else:
        a = '#'
        for i in s.split():
            a += i.capitalize()
            print(a)
        if len(a) > 140:
            return False
        else:
            return a