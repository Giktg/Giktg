def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()
    key_length = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            shift = ord(keyword[i % key_length]) - ord("A")
            ciphertext += alphabet[(alphabet.find(plaintext[i]) + shift) % 26]
        elif plaintext[i] in alphabet_low:
            shift = ord(keyword[i % key_length]) - ord("a")
            ciphertext += alphabet_low[(alphabet_low.find(plaintext[i]) + shift) % 26]
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()
    key_length = len(keyword)

    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            shift = ord(keyword[i % key_length]) - ord("A")
            plaintext += alphabet[(alphabet.find(ciphertext[i]) - shift) % 26]
        elif ciphertext[i] in alphabet_low:
            shift = ord(keyword[i % key_length]) - ord("a")
            plaintext += alphabet_low[(alphabet_low.find(ciphertext[i]) - shift) % 26]
        else:
            plaintext += ciphertext[i]

    return plaintext
