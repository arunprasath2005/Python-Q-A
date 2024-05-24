''' Leap Year Program in Python '''

year = int(input('Enter an year : '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('{} is Leap year'.format(year))
else:
    print('{} is not an leap year'.format(year))
