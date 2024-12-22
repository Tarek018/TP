def divide_into_blocks(ascii_string, block_size):
    # Split the string into blocks of the specified size
    blocks = [ascii_string[i:i + block_size] for i in range(0, len(ascii_string), block_size)]

    # If the last block is shorter than block_size, pad it with zeros
    if len(blocks[-1]) < block_size:
        blocks[-1] = blocks[-1].ljust(block_size, '0')

    return blocks


n = input("Enter N: ")
e = input("Enter e: ")
text = input("Enter plain text: ")
ascii_codes = [ord(char) for char in text]
ascii_codes = ''.join(map(str, ascii_codes))

blocks = divide_into_blocks(ascii_codes, len(n)-1)

# Output the result
print(f"Divided Blocks: {blocks}")
for block in blocks:
  cypher = pow(int(block),int(e)) % int(n)
  print(cypher)