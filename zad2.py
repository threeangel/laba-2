seat_number = int(input("Enter seat number: "))

if seat_number < 1 or seat_number > 64:
    print("Invalid seat number")
elif seat_number % 8 == 1 or seat_number % 8 == 4:
    print("Seat", seat_number, "is a lower berth in a compartment")
elif seat_number % 8 == 2 or seat_number % 8 == 5:
    print("Seat", seat_number, "is an upper berth in a compartment")
elif seat_number % 8 == 3 or seat_number % 8 == 6:
    print("Seat", seat_number, "is a lower berth in a side")
else:
    print("Seat", seat_number, "is an upper berth in a side")