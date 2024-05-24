''' Find the Greatest of the Three Numbers​ in Python '''

n1 = int(input('Enter the number 1: '))
n2 = int(input('Enter the number 2: '))
n3 = int(input('Enter the number 3: '))

if n1>n2 and n1>n3:
    print('{} is greater than {} and {}'.format(n1,n2,n3))
elif n2>n1 and n2>n3:
    print('{} is greater than {} and {}'.format(n1,n1,n3))
else:
    print('{} is greater than {} and {}'.format(n3,n1,n2))
