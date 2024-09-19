n = input('enter value: ')

count = 0
for i in n:
    if i.islower():
        print(i,end='')
        count += 1
print()
print(f'{count} is count of lower chr')
