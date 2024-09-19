#stop loop using index
n = input('enter value: ') # messissipi

for index, val in enumerate(n):
    if index == 6:
        break
    print(val,end='')
