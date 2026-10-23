n = int(input("Enter a positive whole number: "))

while n < 1:
    print("Invalid input. Number must be at least 1.")
    n = int(input("Enter a positive whole number: "))

total = 0

for number in range(1, n + 1):
    cube = number ** 3
    print("Cube of", number, "is", cube)
    total = total + cube

print("Total of the cubes:", total)