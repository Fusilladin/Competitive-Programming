def calculate_1RM(w, r):
    if r == 1:
        return round(w)
    elif r == 0:
        return 0
    else:
        x = round(w*(1 + (r/30)))
        y = round((100*w)/(101.3-(2.67123*r)))
        z = round(w*(r**0.1))
        return max(x,y,z)