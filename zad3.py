def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "- Високосный год")
    else:
        print("Не високосный год")

year = int(input("Введите год: "))
is_leap_year(year)