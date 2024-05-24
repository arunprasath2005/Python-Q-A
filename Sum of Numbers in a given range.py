''' Find the Sum of Numbers in a given Range in Python '''

n1 = int(input('Enter the number 1: '))
n2 = int(input('Enter the number 2: '))

sum = 0 
for i in range(n1,n2+1):
    sum = sum + i

print(sum)
