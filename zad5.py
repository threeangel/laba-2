n = int(input("Enter the number of words: "))
result = ""

for i in range(n):
    word = input("Enter word: ")
    result += word + " "

print("Result:", result)