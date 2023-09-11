# Initial sequence
seq = [1, 0, 1, 1, 0]

# Determine the number of terms to calculate
num_terms = 17

# Generate the sequence
for n in range(num_terms - len(seq)):
    # Calculate the new term
    new_term = seq[n] ^ seq[n + 1] ^ seq[n + 4]
    seq.append(new_term)

if __name__ == "__main__":
    print(''.join(map(str, seq)))

