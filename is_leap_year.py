#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))
