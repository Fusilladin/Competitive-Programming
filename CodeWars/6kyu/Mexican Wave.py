def wave(ppl):
    a = []
    chars = list(ppl)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            a.append(''.join(copy))
    return a
        
    