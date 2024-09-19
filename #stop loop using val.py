#stop loop using val
n = input('enter value: ')  #python

for i in n:
    if i == 'o':
        break
    print(i,end='')
print()

print('-'*50)

i = 0
while i<len(n):
    if n[i] == 'h':
        break
    print(n[i],end='')
    i+=1
print()
print('-'*50)



