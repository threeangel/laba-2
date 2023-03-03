color1 = input("Enter the first primary color: ")
color2 = input("Enter the second primary color: ")

if color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("Purple")
elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("Orange")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Green")
else:
    print("Error: Invalid color input")