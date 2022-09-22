def score(dice):
    points = 0
    for i in dice:
        cnt = dice.count(i)
        if cnt >= 3:
            ash = {1: 1000,
                   6: 600,
                   5: 500,
                   4: 400,
                   3: 300,
                   2: 200
                }
            points += ash[i]
            count = 0
            while count < 3:
                dice.remove(i)
                count+=1
    for j in dice:
        cnt = dice.count(j)
        print(j,'after pop',cnt)
        if int(j) == 1:
            points += 100
        elif int(j) == 5:
            points += 50
        else:
            pass
    return points
        