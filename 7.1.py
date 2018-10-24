fand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()##to remove the blank 
    if line.startswith('From:'):
        print(line)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
