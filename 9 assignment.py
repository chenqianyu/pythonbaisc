name = input("Enter file:")
dic = dict()
lis = list()
count = 0
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        lis.append(words[1])
        count = count + 1
        
for number in lis:
    dic[number] = dic.get(number,0)+1

some = None
any = None

for K,V in dic.items():
    if some == None or any < V:
        some = K
        any = V

print(some,any)
