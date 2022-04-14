from cs50 import get_int
while True:

    height = get_int("height: ")

    if height > 0 and height < 9:

        break

for i in range(height):
    for j in range(i + 1, height):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print("\n", end="")