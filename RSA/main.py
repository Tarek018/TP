def divide_into_blocks(ascii_string, block_size):
    blocks = [ascii_string[i:i + block_size] for i in range(0, len(ascii_string), block_size)]

    if len(blocks[-1]) < block_size:
        blocks[-1] = blocks[-1].ljust(block_size, '0')

    return blocks

n = input("Enter N (public modulus): ")
e = input("Enter e (public exponent): ")
text = input("Enter plain text: ")

ascii_codes = ''.join(f"{ord(char):03d}" for char in text) 
block_size = len(n) - 1 

blocks = divide_into_blocks(ascii_codes, block_size)

cipher_blocks = []
for block in blocks:
    cypher = pow(int(block), int(e), int(n))
    cipher_blocks.append(cypher)

cipher_blocks = []
for block in blocks:
    cipher = pow(int(block), int(e), int(n))
    cipher_blocks.append(str(cipher)) 

print(f"Divided Blocks: {blocks}")
print("Encrypted Cipher Blocks:")
print(" ".join(cipher_blocks)) 
