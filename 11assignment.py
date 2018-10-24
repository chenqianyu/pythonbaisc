import re
fhand = open("C:\\Users\\jerry\\Desktop\\destop.txt")
asy = list()
for line in fhand:
    line = line.rstrip()
    y = re.findall('[0-9]',line)
    
    if len(y)>0:
        print(y)
        for i in range(len(y[0])):
            asy.append(int(y[0][i]))
##sum up the asy
print(int(asy[0]))
count = 0
for i in range(len(asy)):
    count = count + int(asy[i])

print(count)
print(len(asy))

fhand.close()

