def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "- leap year")
    else:
        print("This is not a leap year")

year = int(input("Enter year: "))
is_leap_year(year)