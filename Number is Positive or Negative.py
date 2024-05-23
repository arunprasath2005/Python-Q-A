''' Python Program to check if a Number Is Positive Or Negative '''

n = int(input('Enter an number : '))
if n == 0 :
    print('Zero')
elif n>0:
    print('{} is positive number'.format(n))
else:
    print('{} is negative number'.format(n))
