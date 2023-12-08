# Cryptography Course Codes

This repository contains code implementations for various cryptographic algorithms and functions. These codes were developed for a Cryptography course and cover a range of concepts and techniques.

## Table of Contents

- [phi_calculator.py](#phi_calculatorpy)
- [vigenere_key_extractor.py](#vigenere_key_extractorpy)
- [vigenere_breaker.py](#vigenere_breakerpy)
- [square_and_multiply.py](#square_and_multiplypy)
- [pollard_rho.py](#pollard_rhopy)
- [prime_factorization.py](#prime_factorizationpy)
- [calculate_ord.py](#calculate_ordpy)
- [decrypt_caesar_moving-freq.py](#decrypt_caesar_moving-freqpy)
- [LFSR-KEY](#lfsr-key.py)
- [hill_cipher_decrypt.py](#hill_cipher_decryptpy)
- [fermat_factors.py](#fermat_factorspy)
- [count_letter_frequency.py](#count_letter_frequencypy)
- [ax_b_mod_n_solver.py](#ax_b_mod_n_solverpy)
- [affine_cipher_key_generator.py](#affine_cipher_key_generatorpy)

## Contents Description

### phi_calculator.py

The program includes functions to find numbers coprime to a given number 'x' and calculates Euler's Totient Function ('phi') for 'x' -> ϕ(n).

- Input:
An integer value 'x' for which coprime numbers are calculated.
- Output:
List of numbers coprime to 'x'.
Value of Euler's Totient Function ('phi') for 'x'.

### vigenere_key_extractor.py

The script extracts the Vigenère cipher key given a pair of plain and encrypted texts of the same length.

- Input:
plain_text: The original text.
    * encrypted_text: The text after encryption using the Vigenère cipher.
    * key_length: The length of the Vigenère cipher key.
- Output: The extracted Vigenère cipher key.

### vigenere_breaker.py

The script attempts to break a Vigenère cipher by employing statistical analysis and frequency examination of the ciphertext.

- Input:
    * my_str: The encrypted text (ciphertext) that needs to be decrypted.
    * max_key_size: The maximum expected key size used in the Vigenère cipher.
- Output:
The discovered key used for encryption.
The decrypted text.

### square_and_multiply.py

The script performs modular exponentiation using the Square and Multiply algorithm.

- Input:
    * x: The base value.
    * n: The exponent.
    * m: The modulus.
- Output:  The result of x^n mod m using the Square and Multiply algorithm.

### pollard_rho.py

The script implements Pollard's Rho algorithm to factorize a given integer.

- Input:
    * n: The number to factorize.
- Output:
One of the divisors of the given number, found using Pollard's Rho algorithm.

### prime_factorization.py

The script calculates the prime factorization of a given number.

- Input:
    * n: The number for which prime factors are calculated.
- Output:
The prime factorization of the input number.

### calculate_ord.py

The script calculates the order of an element 'a' within the group Z*n.

- Input:
    * n: The size of the group Zn.
    * a: The number 'a' within the group.
- Output: The order of the element 'a' within the group Zn.

### decrypt_caesar_moving-freq.py

The script attempts to decrypt a Caesar ciphered text based on letter frequency analysis.

- Input: 
    * ciphertext: The encrypted text to be decrypted using the Caesar cipher.
-Output:
The decrypted message based on letter frequency analysis and Caesar cipher decryption.

### LFSR-KEY.py

The script generates a sequence based on the given initial sequence using a specified recurrence relation.

- Input:
    * seq: The initial sequence.
    * num_terms: The number of terms to calculate in the sequence.
- Output:
The generated sequence based on the specified recurrence relation.

### hill_cipher_decrypt.py

The script performs decryption of a Hill ciphered message using a known plaintext attack.

- Input:
    * original_message: The original (known) message.
    * encrypted_message: The encrypted message.
    * matrix_size: The size of the matrix used in the Hill cipher.
- Output:
The decryption key matrix.

### fermat_factors.py

The script utilizes Fermat's factorization method to factorize a given positive integer.

- Input:
    * n: The positive integer to be factorized.
- Output:
The factors of the input positive integer.

### count_letter_frequency.py

The script counts the frequency of each alphabet letter in a given text and displays the results in descending order of frequency.

- Input:
    * text: A string containing the text to be analyzed for letter frequency.
- Output:
The script prints each letter found in the text along with its frequency, sorted in descending order of occurrence.

### ax_b_mod_n_solver.py

This script utilizes the Extended Euclidean Algorithm to solve linear congruence equations of the form ax≡bmodn. It aims to find distinct solutions for x given a, b, and n as input parameters.

- Input:
Values for a, b, and n representing ax≡bmodn equation.
- Output:
The script provides the distinct solutions for x that satisfy the linear congruence equation ax≡bmodn if they exist.

### affine_cipher_key_generator.py

This script facilitates the generation of keys for the Affine Cipher, a type of substitution cipher.

- Input:
    * ciphertext: The encrypted text obtained from the Affine Cipher.
    * plaintext: The corresponding decrypted text used to generate the ciphertext.
- Output:
The script calculates and displays the keys necessary for the Affine Cipher encryption and decryption functions based on the provided ciphertext and plaintext.