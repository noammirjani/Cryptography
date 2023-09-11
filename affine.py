def find_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def affine_keys(plain, cipher):
    m = 26
    plain = [ord(c) - ord('a') for c in plain if c != ' ']
    cipher = [ord(c) - ord('a') for c in cipher if c != ' ']

    for i in range(1, len(plain)):
        if plain[i] != plain[0] and cipher[i] != cipher[0]:
            potential_a = (cipher[i] - cipher[0]) * find_inverse(plain[i] - plain[0], m) % m
            if gcd(potential_a, m) == 1:
                a = potential_a
                b = (cipher[i] - a * plain[i]) % m
                return a, b

    return None, None


def main():
    ciphertext = "vielm bdugb oujld iglof ltbmc lbohl".lower()
    plaintext = "VICTO RHASR EADTH ISTEX TFROM TRENT ".lower()

    a, b = affine_keys(plaintext, ciphertext)

    if a and b:
        print("Encryption function: E(x) = ({}x + {}) mod 26".format(a, b))
        print("Decryption function: D(x) = {}(x - {}) mod 26".format(find_inverse(a, 26), b))
    else:
        print("No suitable key found.")


if __name__ == "__main__":
    main()
