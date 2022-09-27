def valid_parentheses(par):
    count = 0
    for i in par:
        if i == "(":
            count+=1
        elif i == ")":
            count-=1
            if count < 0:
                return False
            else:
                pass
        else:
            pass 
    if count != 0:
        return False
    else:
        return True
    