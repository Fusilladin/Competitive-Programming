def spin_words(sent):
    sent = sent.split(' ')
    a = []
    for i in sent:
        if len(i) > 4:
            a.append(i[::-1])
        else:
            a.append(i)
    a = ' '.join(a)
    return a
    