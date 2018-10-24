##counting the words
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('words',words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0)+1
#print('counts',counts)

## use for the list the words
for key in counts:
    print(key,counts[key])

##flexible to show the key or value or translate to a list
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

##
for aaa,bbb in counts.items():
    print(aaa,bbb)
