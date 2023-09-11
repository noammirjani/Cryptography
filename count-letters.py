from collections import Counter


def count_letters(text):
    # Count the occurrence of each letter in the text
    counts = Counter(text.lower())

    # Filter out non-alphabet characters
    counts = {k: v for k, v in counts.items() if k.isalpha()}

    # Sort by frequency in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_counts:
        print(f"Letter: {letter}, Frequency: {count}")


if __name__ == '__main__':
    # example usage:
    text = "NEXS MPMF WPBX NKPG XGDD VBFK"
    count_letters(text)

