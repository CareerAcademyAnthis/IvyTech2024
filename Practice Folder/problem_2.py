year = int(input('Enter a year: '))

if (year % 400) == 0:
    is_leap = True
elif(year % 100) == 0:
    is_leap = False
elif(year % 4) == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")