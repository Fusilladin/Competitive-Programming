def DNA_strand(dna):
    ref = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"
    }
    return ''.join([ref[x] for x in dna])

--

def DNA_strand(dna):
    print(dna,type(dna))
    a = []
    for i in dna:
        print(i)
        if i == 'A':
            a.append('T')
        elif i == 'T':
            a.append('A')
        elif i == 'C':
            a.append('G')
        elif i == 'G':
            a.append('C')
        else:
            pass
    return ''.join(a)