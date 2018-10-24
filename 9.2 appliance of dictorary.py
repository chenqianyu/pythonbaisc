##9.2 Dictionaries and files

fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

##or
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)

