'''
      NOAM MIRJANI & SAMI
      315216515    &
'''

import string

ENGLISH_LETTER_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                       'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41,
                       'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77,
                       'J': 0.15,
                       'X': 0.15, 'Q': 0.10, 'Z': 0.07}

MAX_KEY_SIZE = 6
ENGLISH_LETTERS_AMOUNT = 26


def vector_mult(B_vector: dict, englishLetterFreq_vector: dict, shift: int):
    """
    Calculate the dot product of two dictionaries of letter frequencies, B_vector and englishLetterFreq_vector, after
    shifting the englishLetterFreq_vector by shift letters.

    :param B_vector: A dictionary of letter frequencies for a block of ciphertext.
    :param englishLetterFreq_vector: A dictionary of letter frequencies for the English language.
    :param shift: The number of letters to shift the englishLetterFreq_vector by.
    :return: The dot product of the two vectors.
    """
    result = 0

    for i in range(ENGLISH_LETTERS_AMOUNT):
        result += B_vector[chr(ord('A') + i)] * englishLetterFreq_vector[
            chr((ord('A') + ((i + shift) % ENGLISH_LETTERS_AMOUNT)))]

    return result


def find_shift(B_vector, englishLetterFreq_vector) -> str:
    """
    Find the shift amount that maximizes the dot product between B_vector and englishLetterFreq_vector, and return
    the corresponding letter.

    :param B_vector: A dictionary of letter frequencies for a block of ciphertext.
    :param englishLetterFreq_vector: A dictionary of letter frequencies for the English language.
    :return: The letter corresponding to the shift amount that maximizes the dot product.
    :rtype: str
    """
    max_result = 0
    shift = 0

    print('The results of the vector mult: ')
    for i in range(ENGLISH_LETTERS_AMOUNT):
        result = vector_mult(B_vector, englishLetterFreq_vector, i)
        print(f'The result of a vector product for B, {i} is: {result}')
        if result > max_result:
            max_result = result
            shift = i

    char_shift = chr(ord('A') + 26 - shift)
    print(f'Found the letter {char_shift}')
    print('\n-----------------------')
    return str(char_shift)  # convert the character to a string


def divide_to_blocks(ciphertext, key_size):
    """
    Divide the ciphertext into blocks of length key_size.

    :param ciphertext: The ciphertext to be
    :param key_size: The size of the key.
    :return: A list of ciphertext blocks and a dictionary of letter frequencies for the English language.
    """
    # split the ciphertext into blocks
    ciphertext_blocks = [''] * key_size
    for i, char in enumerate(ciphertext):
        ciphertext_blocks[i % key_size] += char

    englishLetterFreq_vector = dict.fromkeys(string.ascii_uppercase, 0)
    for char, freq in ENGLISH_LETTER_FREQ.items():
        englishLetterFreq_vector[char] = freq / 100
    return ciphertext_blocks, englishLetterFreq_vector


def decode_vigenere_cipher(ciphertext: str) -> str:
    """
    Decode a ciphertext encrypted with the Vigenere cipher.
    :param ciphertext: The ciphertext to be decoded.
    :return: The decoded message.
    """
    ciphertext = ciphertext.upper()
    key_size = get_key_size(ciphertext, MAX_KEY_SIZE)
    ciphertext_blocks, englishLetterFreq_vector = divide_to_blocks(ciphertext, key_size)
    key = get_key(ciphertext_blocks, key_size, englishLetterFreq_vector)
    return decode_message(ciphertext, key, key_size)


def get_key(ciphertext_blocks: list, key_size: int, englishLetterFreq_vector) -> str:
    """
    Get the key for the Vigenere cipher.
    :param ciphertext_blocks: text blocks
    :param key_size: size of the key
    :param englishLetterFreq_vector:  dictionary of letter frequencies for the English language
    :return:  The key for the Vigenere cipher.
    """
    key = ''
    for i in range(key_size):
        B_vector = dict.fromkeys(string.ascii_uppercase, 0)
        block = ciphertext_blocks[i]
        print_letters_frequency(block, i)

        # calculate B vector
        for char in string.ascii_uppercase:
            letter_freq = block.count(char)
            B_vector[char] = letter_freq / len(block)

        key_letter = find_shift(B_vector, englishLetterFreq_vector)
        key += key_letter

    key = "".join(key)
    print(f'The key size is: {key_size}')
    print(f'The key is: {key}')
    print('\n-----------------------')
    return key


def decode_message(ciphertext, key, key_size) -> str:
    """
    Decode the message using the key.
    :param ciphertext: text to decode
    :param key: key
    :param key_size:  size of the key
    :return:  decoded message
    """
    plaintext = ''
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % key_size]) - ord('A')
        plaintext += chr((ord(char) - ord('A') - shift) % ENGLISH_LETTERS_AMOUNT + ord('A'))

    return plaintext.lower()


def get_key_size(message: str, max_key_size: int) -> int:
    curr_match = 0
    size = 0
    max_match = 0

    if max_key_size is not None:
        max_size = max_key_size
    else:
        max_size = len(message)

    for i in range(1, max_size + 1):
        for j in range(len(message) - i):
            if message[j] == message[j + i]:
                curr_match += 1
        if curr_match > max_match:
            max_match = curr_match
            size = i
        curr_match = 0

    return size


def print_letters_frequency(sentence: str, i: int):
    """
    Print the frequency of each letter in the sentence.
    :param sentence:  The sentence to be analyzed.
    :param i:  The index of the block.
    """
    letter_freq = dict.fromkeys(string.ascii_uppercase, 0)
    for char in sentence:
        if char.isalpha():
            letter_freq[char.upper()] += 1

    print(f'Letters frequency for block {i}:')
    for char, freq in letter_freq.items():
        print(f'{char}: {freq}')


if __name__ == '__main__':
    with open('ciphertext.txt', 'r') as f:
        encoded_message = f.read().upper().replace(" ", "").strip()

    print(decode_vigenere_cipher(encoded_message))

