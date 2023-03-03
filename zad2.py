seat_number = int(input("Введите место: "))

if seat_number < 1 or seat_number > 64:
    print("введи норм место пж(")
elif seat_number % 8 == 1 or seat_number % 8 == 4:
    print("Место", seat_number, "Нижнее место в купе")
elif seat_number % 8 == 2 or seat_number % 8 == 5:
    print("Место", seat_number, "Верхнее место в купе")
elif seat_number % 8 == 3 or seat_number % 8 == 6:
    print("Место", seat_number, "Нижнее боковое место")
else:
    print("Место", seat_number, "Верхнее боковое место")