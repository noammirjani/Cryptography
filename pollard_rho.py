import random
import math


def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def PollardRho(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2
    x = 2
    y = x
    c = 1
    d = 1

    i = 0
    print(f"{'Index':<10}{'X Value':<15}{'Y Value':<15}{'GCD':<10}")
    print(f"{i:<10}{x:<15}{y:<15}{d:<10}")
    i += 1
    while d == 1:
        x = (modular_pow(x, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        d = math.gcd(abs(x - y), n)
        print(f"{i:<10}{x:<15}{y:<15}{d:<10}")
        i += 1
        if d == n:
            return PollardRho(n)
    return d


if __name__ == "__main__":
    n = 256961
    print(f"One of the divisors for {n} is {PollardRho(n)}")
