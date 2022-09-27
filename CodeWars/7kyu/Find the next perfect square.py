def find_next_square(sq):
    print(sq)
    if sq == 0:
        return 1
    elif sq == 1:
        return 4
    else:
        for i in range(sq):
            if i*i > sq:
                return -1
            elif sq == 0:
                return 0
            elif i*i == sq:
                return (i+1)*(i+1)

            else:
                pass
    
