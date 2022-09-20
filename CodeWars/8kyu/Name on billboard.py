def billboard(name, price=30):
    
    total = 0
    for l in name:
        total = total + price
    return total