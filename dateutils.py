"""
Module for validating dates, leap year checks, and calculating age in days.
"""

def is_leap_year(year):
    """Return True if the year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in a month for a given year."""
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def is_valid_date(year, month, day):
    """Check whether a given date is valid."""
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(year, month):
        return False
    return True

def date_to_days(year, month, day):
    """Convert a date to the number of days since 01/01/0001."""
    total_days = 0
    for year_index in range(1, year):
        total_days += 366 if is_leap_year(year_index) else 365
    for month_index in range(1, month):
        total_days += days_in_month(year, month_index)
    total_days += day
    return total_days

def days_between(year1, month1, day1, year2, month2, day2):
    """Calculate number of days between two dates."""
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0
    days1 = date_to_days(year1, month1, day1)
    days2 = date_to_days(year2, month2, day2)
    return max(0, days2 - days1)

def age_in_days(year, month, day):
    """Calculate age in days from a birthdate to today."""
    # Server date fixed as 2025-05-26
    today_year = 2025
    today_month = 5
    today_day = 26

    if not is_valid_date(year, month, day):
        return 0
    return days_between(year, month, day, today_year, today_month, today_day)
