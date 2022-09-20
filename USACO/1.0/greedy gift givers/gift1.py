# Greedy gift givers

# friends: 3-9 
# name length: 14 max
# no fractions,  additional dollar goes to givers account
# Goal: calculate list of name
    #  sublist of whom they're giving money to
    # amount of money each person ends up with
# input: 
    # Line 1 - int: num of people
    # subsequent lines: names of all friends
    # final name line: name of giver
    # next line amount of total money giving and num of friends giving to 
# output:
    # num of friends of lines
    # each line is name of person and ending amount of money

# reading the file 
f = open(r"C:\Users\userTK427\Desktop\Studying\Competitive Programming\USACO\1.0\greedy gift givers\gift1.in","r")
count = 0
players = int(f.readline())
lines = f.readlines()

for line in lines:
    count += 1
    #print(line.strip())

# printing names of the first set of names
# adding them into a dict with their starting amount of money

count = 0
d = {}
for p in lines:
    if count < players:
        d[count] = p.strip(),0
        count += 1
        continue
    else:
        #print(d)
        break
 
# search for name 
# find next line containing money and number of friends giving to
# find next line containing friend names
#print(lines[0])
count = 0
for p in d:
    var = (d[count])
    name = (var[0])
    break
count = 0
#print(name)

# searching for next line after name to find the integers for the money and num of friends given to

for line in lines:
    if name in line:
        next = (lines[count])
        #print(next)
        list = (next)
        count = 0
        print(list)
        
        for i in list:
            try:
                i = int(i)
                #print(i)
                #print('Count',count)
                if count == 0:
                    money = i
                    #print(money)
                    count+=1
                elif count == 1:
                    friends = i
                else:
                    print("count",count)
            except ValueError as ve:
                # print('test')
                # Handle the exception
                pass
            #print(money,friends)
    else:
        count+=1
        pass

f.close()


