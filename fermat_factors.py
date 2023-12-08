from math import ceil, sqrt


def FermatFactors(n):
    # Print header for table
    print(f"{'a':<10}{'b':<10}")

    # since fermat's factorization applicable
    # for odd positive integers only
    if n <= 0:
        return [n]

    # check if n is a even number
    if (n & 1) == 0:
        return [n / 2, 2]

    a = ceil(sqrt(n))

    # if n is a perfect root,
    # then both its square roots are its factors
    if a * a == n:
        return [a, a]

    while (True):
        b1 = a * a - n
        b = int(sqrt(b1))
        print(f"{a:<10}{sqrt(b1):<10}")
        if b * b == b1:
            print("the x value: ", a)  # that is the x to stop the process
            print("the equation square root: ", b)
            break
        else:
            a += 1
    print(n, "=", a, "^2 -", b, "^2", "---->" "(", a, "-", b, ")(", a, "+", b, ")",  "---->", a - b, "*", a + b)
    return [a - b, a + b]


if __name__ == "__main__":
    print(FermatFactors(26069))
