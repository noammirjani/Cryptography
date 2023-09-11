def decrypt_caesar(ciphertext):
    # Define the most frequent letter in the language
    language_frequencies = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                            'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                            'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                            'q': 0.10, 'z': 0.07}

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
    most_frequent_message_letter = sorted_freq[0][0]  # Get the most frequent message letter
    for freq_pair in sorted_freq:
        # Define the most frequent unused letter in the language
        most_frequent_language_letter = max(
            [(k, v) for k, v in language_frequencies.items() if k not in used_letters],
            key=lambda x: x[1])[0]
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

        print("most freq language letter ", most_frequent_language_letter,
              "\nmost freq message letter ", most_frequent_message_letter, "freq ", freq_pair[1])
        print("Shift value:", most_frequent_message_letter, '-', most_frequent_language_letter, '=',
              ord(most_frequent_message_letter)-97, '-', ord(most_frequent_language_letter)-97, '=', shift)
        print("Decrypted message:", plaintext)
        print("----")


if __name__ == "__main__":
    # ciphertext = 'vielm bdugb oujld iglof ltbmc lbohl'
    ciphertext = 'sfzql oexpo bxaqe fpqbu qcolj qobkq '
    decrypt_caesar(ciphertext.upper())
