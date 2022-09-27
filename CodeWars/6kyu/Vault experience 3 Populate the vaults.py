def populate_my_vault(dwel):
    if dwel == 0:
        return (0,0,0)
    elif dwel == 1:
        return (1,0,0)
    else:
        if dwel <= 50: 
            if dwel % 2 == 0:
                mngr = 1
                female = dwel // 2
                male = (dwel // 2) - 1
            elif dwel % 2 == 1:
                mngr = 1
                female = (dwel // 2) +1
                male = (dwel // 2) -1
        elif dwel > 50:
            if dwel % 2 == 0:
                mngr = 2
                female = (dwel // 2) -1
                male = (dwel // 2) -1
            elif dwel % 2 == 1:
                mngr = 2
                female = (dwel // 2)
                male = (dwel // 2) -1
    return (mngr,female, male)
    
    
    #return # (overseers_count, regular_females_count, regular_males_count)