"""
ID: joegodi1
LANG: PYTHON3
TASK: ride
"""

# reading the file and setting a variable to each line
f = open(r'C:\Users\userTK427\Desktop\Studying\Competitive Programming\USACO\1.0\ride.in','r')
lines = f.readlines()
f.close()
ufo = lines[0]
group = lines[1]
# print("Read good")

# removing the \n character in each var
ufo = ufo.rstrip()
group = group.rstrip()
# print("strip good")
  
# splitting the string into seperated chars
def split_ufo(ufo):
	return [c for c in ufo]
ufo = (split_ufo(ufo))	
def split_group(group):
	return [c for c in group]
group = (split_group(group))
# print("char good")

# changing chars into nums and multiplying each of them together
result1 = 1
result2 = 2

output = []
for char in ufo:
	num = ord(char) - 64
	output.append(num)
for i in output:
	result1 = result1 * i	
print(result1)
output = []
for char in group:
	num = ord(char) - 64
	output.append(num)
for i in output:
	result2 = result2 * i
print(result2)

# finding the product mod of 47 for each var
result1 = result1 % 47 
result2 = result2 % 47
# print("var good")

# comparing outputs 
if result1 == result2:
	answer = "GO"
else:
	answer = "STAY"
# print("end good")

# writing answer to file ride.out
f = open(r"C:\Users\userTK427\Desktop\Studying\Competitive Programming\USACO\1.0\ride.out", "w")
f.write(answer+"\n")
f.close()