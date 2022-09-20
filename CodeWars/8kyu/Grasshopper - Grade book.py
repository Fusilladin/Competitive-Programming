def get_grade(s1, s2, s3):
    x = (s1+s2+s3) / 3
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'
    
    