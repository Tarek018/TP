def divide_into_blocks(ascii_string, block_size):
    # Split the string into blocks of the specified size
    blocks = [ascii_string[i:i + block_size] for i in range(0, len(ascii_string), block_size)]

    # If the last block is shorter than block_size, pad it with zeros
    if len(blocks[-1]) < block_size:
        blocks[-1] = blocks[-1].ljust(block_size, '0')

    return blocks

# Input RSA parameters and plaintext
n = input("Enter N (public modulus): ")
e = input("Enter e (public exponent): ")
text = input("Enter plain text: ")

# Convert plaintext to numeric representation
ascii_codes = ''.join(f"{ord(char):03d}" for char in text)  # Ensure 3-digit ASCII values
block_size = len(n) - 1  # Block size based on modulus length

# Divide into blocks
blocks = divide_into_blocks(ascii_codes, block_size)

# Perform RSA encryption on each block
cipher_blocks = []
for block in blocks:
    cypher = pow(int(block), int(e), int(n))  # Modular exponentiation
    cipher_blocks.append(cypher)

# Output the result
print(f"Divided Blocks: {blocks}")
print("Encrypted Cipher Blocks:")
for block in cipher_blocks:
    print(block)
