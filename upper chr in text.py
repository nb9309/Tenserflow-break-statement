n = input('enter value: ').title()
count = 0
for i in n:
    if i.isupper():
        print(i,end='')
        count += 1
print()
print(f'{count} is count')

