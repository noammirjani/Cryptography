def calculate_ord(n, a):
    if n <= 0:
        return "Error: Invalid group size"
    if a == 0:
        return "Error: 'a' must be a non-zero number"

    for exponent in range(1, n + 1):
        if pow(a, exponent, n) == 1:
            return exponent

    return "Infinite order (e = n)"


if __name__ == '__main__':
    # Get inputs from the user
    group_size = int(input("Enter the size of the group Z*n: "))
    number_a = int(input("Enter a number 'a': "))

    # Calculate and print the ord(a)
    result = calculate_ord(group_size, number_a)
    print(f"The ord(a) is: {result}")
