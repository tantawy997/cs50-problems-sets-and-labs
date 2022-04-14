from cs50 import get_float

# a function that gets an input from the user and yileds how much coins used for the change


def main():
    coins = 0
    dollar = get_float("chage set: ")
    while dollar <= 0:
        dollar = float(input("change set: "))
    # how much cents from the dollar

    cents = int(round(dollar * 100))
    while cents >= 25:
        cents = cents - 25
        coins += 1

    while cents >= 10:
        cents = cents - 10
        coins += 1

    while cents >= 5:
        cents = cents - 5
        coins += 1

    while cents >= 1:
        cents = cents - 1
        coins += 1
    return coins

# calling the function to get the calculated coins


coins = main()
print("coins", coins)