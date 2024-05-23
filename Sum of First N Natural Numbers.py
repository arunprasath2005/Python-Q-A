''' Python Program to Find the Sum of First N Natural Numbers '''

n = int(input('Enter an number: '))
val = 0
for i in range(0,n+1):
    val =val + i

print(val)
