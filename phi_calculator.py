import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_equal_to_1_list(x):
    numbers = []
    for num in range(x + 1):
        if gcd(num, x) == 1:
            numbers.append(num)
    return numbers


if __name__ == "__main__":
    # Get user input for x
    x = int(input("Enter a value for x: "))

    # Generate and print the list of numbers
    result = gcd_equal_to_1_list(x)
    print("Tout les nombre zar a x sont:")
    print(result)
    print("phi of n is:", len(result))
