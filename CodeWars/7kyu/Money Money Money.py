def calculate_years(principal, interest, tax, desired):
    count = 0
    if principal >= desired:
        return 0
    else:
        while principal < desired:
            x = principal*interest
            y = x*tax
            x = x-y
            principal += x
            count += 1
        return count 