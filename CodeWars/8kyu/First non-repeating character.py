def first_non_repeating_letter(word):
    wrd = word.lower()
    for i in word:
        if wrd.count(i.lower()) == 1:
            return i
        
    return ''