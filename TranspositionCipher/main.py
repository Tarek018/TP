def split_text_by_key(text: str, key: int) -> list:
    return [text[i:i + key] for i in range(0, len(text), key)]

import re

plaintText = ""
with open("E:/Learning projects/TP/TranspositionCipher/plaintText.txt", "r") as file:
      plaintText = file.read()
      plaintText = re.sub(r'[^A-Za-z0-9 ]+', '', plaintText)


plaintText = "".join(plaintText.split())
key = input("Enter key :")
while not key.isdigit():
    key = input("Enter key :")

while int(key) >= len(plaintText) or int(key) < 1:
  key = input("Enter key :")


x = ""
y = ""


result = split_text_by_key(plaintText, int(key))
for block in result:
  if(len(block) == int(key)):
    y = y + block[-1]
    x = x + block[:-1]
  else: 
    x = x + block


cipherText = x + y
print("The Cipher Text is ==> " + cipherText)