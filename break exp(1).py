n = int(input('enter value: '))
if n<=1:
    print(f'{n} is invalid')
else:
    res = 'prime'
    for i in range(2,n):
        if n%i == 0:
            res = 'not a prime'
            break
    print('{} is {}'.format(n,res))