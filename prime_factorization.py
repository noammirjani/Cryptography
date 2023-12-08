def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def breakdown_to_prime_factors(n):
    if n < 2:
        return ""
    factors = prime_factors(n)
    breakdown = []
    for factor in factors:
        if factor not in breakdown:
            breakdown.append(factor)
            breakdown.extend(breakdown_to_prime_factors(n // factor))
    return breakdown


def format_prime_factors(n):
    breakdown = breakdown_to_prime_factors(n)
    if not breakdown:
        return str(n)
    factor_counts = {}
    for factor in breakdown:
        factor_counts[factor] = factor_counts.get(factor, 0) + 1
    formatted_factors = []
    for factor, count in factor_counts.items():
        if count > 1:
            formatted_factors.append(f"{factor}^{count}")
        else:
            formatted_factors.append(str(factor))
    return "*".join(formatted_factors)


if __name__ == "__main__":
    # Example usage
    number = int(input("Enter a number: "))
    formatted_output = format_prime_factors(number)
    print(f"The prime factorization of {number} is: {formatted_output}")
