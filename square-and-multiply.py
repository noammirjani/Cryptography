def square_and_multiply(x, n, m):
    # Convert n to its binary representation
    binary_n = bin(n)[2:]

    # Initialize result to 1
    result = 1

    # Print header for table
    print(f"{'i':<5}{'ci':<5}{'z^2':<10}{'xz':<10}")

    # Traverse through each bit of the binary representation of n
    for i, bit in enumerate(binary_n):
        # Square the result in each iteration and perform modulus operation
        z_sq = (result ** 2) % m
        result = z_sq

        xz = ''
        # If the bit is '1', multiply by x and perform modulus operation
        if bit == '1':
            result = (result * x) % m
            xz = result

        # Print row of table
        print(f"{i:<5}{bit:<5}{z_sq:<10}{xz:<10}")

    return result


if __name__ == "__main__":
    print("total: ", square_and_multiply(3152, 17, 26069))  # Outputs: 68, which is equal to (5^13) mod 123

