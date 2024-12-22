import string

def caesar_code(Text,key1,key2):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))

    Text_chiffrer = ""

    print(Text)
    for char in Text:
        i=0
        alphabet = string.ascii_lowercase
        char = char.lower()
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key1) % 26
            new_index = (new_index + key2) % 26
            Text_chiffrer = Text_chiffrer + alphabet[new_index]    
        else:
            if char == ' ':
                Text_chiffrer = Text_chiffrer + ' '
            else:
                if char == ',':
                    Text_chiffrer = Text_chiffrer + ','
                else:
                    Text_chiffrer = Text_chiffrer + char
    return Text_chiffrer

def decrypte_caesar_code(Text):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))
    
    k = 0
    k1 = 0
    new_file_path = "decrypted_file.txt"
    plainText = ''


    for k in range(26):
        plainText = plainText + '\n***Pour k1 = '+str(k)+'***\n'
        for k1 in range(26):
            plainText = plainText + '\nk2='+str(k1)+'  ==>  '
            for char in Text:
                alphabet = string.ascii_lowercase
                char = char.lower()
                if char in alphabet:
                    index = alphabet.index(char)
                    new_index = (index - k) % 26
                    new_index = (new_index - k1) % 26
                    plainText = plainText + alphabet[new_index]   
                else:
                    plainText = plainText + char
            k1 = k1 + 1
        plainText = plainText + '\n------------:'
        k=k+1  
    return plainText
