fruit = 'banana'
letter = fruit[1]
print(letter)

print(len(fruit))
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(letter)
    index = index +1

for char in fruit:
    print(char)

s = 'Monty Python'
##search the process from 0 to 5
print(s[0:5])
print(s[6:10])

##more trickly method,don't have to click the begining or the end
fruit = 'banana'
fruit[:3]
fruit[3:]

##the letter of string can not be change, the way to do kis
greeting = 'Hello,world!'
new_greeting = 'J'+greeting[1:]
print(new_greeting)
Jello,world!


##in operator
'a' in banana
##return to true
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines
', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
greet = 'Hello Bob'
nstr = greet.replace('Bob',Jane)
print(nstr)
line =  'Please start with'
line.startswith('P')
