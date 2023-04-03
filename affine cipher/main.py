def decrypt_caesar(ciphertext):
    # Define the most frequent letter in the language
    language_frequencies = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
                            'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
                            'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
                            's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.361, 'x': 0.150,
                            'y': 1.974, 'z': 0.074}

    # Create a dictionary of letter frequencies in the ciphertext
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            if char.lower() in freq:
                freq[char.lower()] += 1
            else:
                freq[char.lower()] = 1

    # Sort the letters in the ciphertext by frequency in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    used_letters = set()
    for freq in sorted_freq:
        # Define the most frequent letter in the message
        most_frequent_message_letter = freq[0]
        # Find the most frequent unused letter in the language
        most_frequent_language_letter = max([(k, v) for k, v in language_frequencies.items() if k not in used_letters], key=lambda x: x[1])[0]
        used_letters.add(most_frequent_language_letter)

        # Calculate the shift value
        shift = (ord(most_frequent_message_letter) - ord(most_frequent_language_letter)) % 26

        # Decrypt the message using the shift value
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    plaintext += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                plaintext += char

        print("most freq language letter ", most_frequent_language_letter, "\n most freq message letter ", most_frequent_message_letter, "freq ", freq[1])
        print("Shift value:", shift)
        print("Decrypted message:", plaintext)
        print("----")


ciphertext = 'hscsy xlmro aiamp pkixe rsxli vvssq'

decrypt_caesar(ciphertext)
