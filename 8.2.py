total = 0
count = 0
while True:
    inp = input('please enter an number:')
    if inp == 'done':break
    try:
        value = float(inp)
        total = total + value
        count = count+1
    except:
        print('invalid number')
average = total/count
print('Average:',average)

##the other way of this
numberlist = list()
while True:
    some = input('Please enter a number:')
    if inp == 'done':break
    try:
        value2 = float(inp)
        numberlist.append(value2)
    except:
        print('invalid number')
average = sum(numberlist)/len(numberlist)
print('average:',average)
##need to memory the number

