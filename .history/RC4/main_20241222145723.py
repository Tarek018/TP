def ksa(key, s):
    """Key Scheduling Algorithm (KSA)"""
    j = 0
    n = len(s)
    
    # Initialisation de S en fonction de la clé
    for i in range(n):
        j = (j + int(s[i]) + ord(key[i % len(key)])) % n
        s[i], s[j] = s[j], s[i]  # Échange des éléments dans S

    return s

def prga(s):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    n = len(s)
    
    while True:
        i = (i + 1) % n
        j = (j + int(s[i])) % n
        s[i], s[j] = s[j], s[i]  # Échange des éléments dans S
        K = s[(int(s[i]) + int(s[j])) % n]
        yield int(K)

def rc4(plaintext, key, s):
    """Chiffrement RC4"""
    # Étape 1 : Key Scheduling Algorithm (KSA)
    s = ksa(key, s)
    
    # Étape 2 : Génération du flux de clés avec PRGA
    keystream = prga(s)
    
    # Étape 3 : Chiffrement par XOR avec le flux de clés
    ciphertext = ''.join(chr(ord(char) ^ next(keystream)) for char in plaintext)
    return ciphertext


# Exemple d'utilisation
p = input("donner moi le text : ")  # Texte en clair
k = ["1", "2", "3", "6"]  # Clé de chiffrement
s = ["0", "1", "2", "3", "4", "5", "6", "7"]  # Tableau d'état initial

# Convertir la clé en une chaîne de caractères pour l'utilisation
key = ''.join(k)

# Chiffrement
ciphertext = rc4(p, key, s)
print(f"Texte chiffré : {ciphertext}")
