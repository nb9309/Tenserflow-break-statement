n = input('enter value: ')
count = 0
for i in n:
    if (not i.isalnum()) and (not i.isspace()):
        print(i)
        count += 1
print(f'{count} is count of special sym')