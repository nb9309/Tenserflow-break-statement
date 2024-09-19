#count of duplicates
n = input('enter value: ')
duplecates ={}
for i in n:
    if i in duplecates:
        duplecates[i] += 1
    else:
        duplecates[i] = 1
for val,count in duplecates.items():
    print('{} ---> {}'.format(val,count))