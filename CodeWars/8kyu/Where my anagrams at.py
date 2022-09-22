def anagrams(word, words):
    a = []
    for i in words:
        if sorted(word) == sorted(i):
            a.append(i)
    return a