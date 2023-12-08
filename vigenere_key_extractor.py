def get_vigenere_key(plain_text, encrypted_text, key_length):
    if len(plain_text) != len(encrypted_text):
        raise ValueError("Plain text and encrypted text must be of the same length")

    plain_text = plain_text.upper()
    encrypted_text = encrypted_text.upper()

    key = ''
    for i in range(key_length):
        plain_segment = plain_text[i::key_length]
        encrypted_segment = encrypted_text[i::key_length]
        key += get_key_for_segment(plain_segment, encrypted_segment)

    return key


def get_key_for_segment(plain_segment, encrypted_segment):
    key_segment = ''
    for p, e in zip(plain_segment, encrypted_segment):
        key_char = (ord(e) - ord(p)) % 26
        key_segment += chr(key_char + ord('A'))
        if p != ' ' or e != ' ':
            print(e, '-', p, '=', ord(e), '-', ord(p), '=', key_char, 'mod26', '=', key_segment[-1])

    return key_segment


if __name__ == '__main__':
    # example usage:
    plain_text =     'PEGG YCAN NOTW RITE TOFE RMAT'
    encrypted_text = 'GSYK PQSR ECLA IWLI KCXI IASL'
    key_length = 1
    print(get_vigenere_key(plain_text, encrypted_text, key_length))
