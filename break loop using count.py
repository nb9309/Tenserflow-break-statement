#break loop using count
n = input('enter value: ') # messissioi

count=0
for i in n:
    if i == 's':
        count += 1
    if count == 4:
        break
    else:
        print('.',i,end=' ')
print('-'*50)

cnt = 0
i = 0
while i < len(n):
    if n[i] == 's':
        cnt = cnt+1
    if cnt == 4:
        break
    print(n[i])
    i = i+1




