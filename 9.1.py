## insert function of dictionary
eng2sp = dict()
eng2sp['one'] = 'uno'
print(eng2sp)

## insert function of multiply value

eng2sp = {'one':'uno','two':'dos','three':'tres'}
print(eng2sp)

## if you want to print the value of it
print(eng2sp['two'])

## if you use in to retrieve the value
'one' in eng2sp
#turn out to be true
'uno' in eng2sp
#turn out to be false

## else if you want to check the value instead of the index,you need to switch to list

vals = list(eng2sp.values())

'uno' in eng2sp
##turn out to be true

eng2sp.get()

## powerful funciton to sort and count the number
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c]+1
print(d)

## the more simple one is that
word = 'brontosaurus'
d = dict()
for c in word:
d[c] = d.get(c,0) + 1  ## d.get(c,0) means that d get c in the dictionary d,if there is not c in the dictionary,then generate one name c
print(d)


