def is_sunday(day, month, year):
    days = days_since_1900(day, month, year)
    return days % 7 == 0

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    return 28

def days_since_1900(day, month, year):
    days = 0
    for i in range(1900, year):
        days += 365
        if is_leap_year(i):
            days += 1
    for i in range(1, month):
        days += days_in_month(i, year)
    days += day
    return days

def problem19():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if is_sunday(1, month, year):
                count += 1
    return count

print(problem19())