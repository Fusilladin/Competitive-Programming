def get_count(sent):
    count = 0
    vowels = {'a','e','i','o','u'}
    for i in sent:
        if i in vowels:
            count+=1
    return count