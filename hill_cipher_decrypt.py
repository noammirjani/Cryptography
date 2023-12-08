import numpy as np


def get_inverse(matrix, modulus):
    # Calculate the inverse of a matrix modulo a given modulus
    try:
        det = int(np.round(np.linalg.det(matrix))) % modulus
        det_inv = pow(det, -1, modulus)
        adjugate_matrix = np.round(det_inv * np.linalg.inv(matrix)).astype(int)
        # Calculate the inverse matrix modulo x
        inverse_matrix = (adjugate_matrix % modulus + modulus) % modulus
        return inverse_matrix
    except np.linalg.LinAlgError as e:
        if 'base is not invertible for the given modulus' in str(e):
            return None
        raise e


def char_to_num(char):
    # Convert a character to its corresponding numeric value
    return ord(char) - ord('A')


def num_to_char(num):
    # Convert a numeric value to its corresponding character
    return chr(num + ord('A'))


def decrypt_hill_cipher(original_message, encrypted_message, matrix_size=None):
    # Convert the input strings to uppercase
    original_message = original_message.upper()
    print(original_message)
    encrypted_message = encrypted_message.upper()
    print(encrypted_message)

    # If matrix size is not provided, calculate it based on the length of the original message
    if matrix_size is None:
        matrix_size = int(np.ceil(np.sqrt(len(original_message))))

    modulus = 26  # Assuming English alphabet

    while True:
        # Select the appropriate number of values from the original and encrypted messages
        original_nums = [char_to_num(char) for char in original_message[0:4]]
        encrypted_nums = [char_to_num(char) for char in encrypted_message[0:4]]

        # Construct the matrices
        original_matrix = np.reshape(original_nums, (matrix_size, matrix_size)).T
        print(original_matrix)
        encrypted_matrix = np.reshape(encrypted_nums, (matrix_size, matrix_size)).T
        print(encrypted_matrix)

        # Find the encryption matrix by multiplying the inverse of the original matrix with the encrypted matrix
        inverse_matrix = get_inverse(original_matrix, modulus)

        if inverse_matrix is not None:
            break  # Exit the loop if an invertible matrix is found

    print("Original Matrix:")
    print(original_matrix)
    print("Encrypted Matrix:")
    print(encrypted_matrix)
    print("Inverse Matrix:")
    print(inverse_matrix)

    encryption_matrix = (encrypted_matrix @ inverse_matrix) % modulus

    print("Encryption Matrix:")
    print(encryption_matrix)

    return encryption_matrix


if __name__ == '__main__':
    # Example usage
    original_message = "VICTO RHASR EADTH ISTEX TFROM TRENT".lower()
    encrypted_message = "lzlgx ujprk uqqxt vnsne uffhj uztol"
    encryption_matrix = decrypt_hill_cipher(original_message, encrypted_message, matrix_size=2)

    # Convert the encryption matrix back to characters
    decryption_key = [[num_to_char(num) for num in row] for row in encryption_matrix]

    print("Decryption key:")
    for row in decryption_key:
        print(" ".join(row))
