def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lalphabet = alphabet.lower()
    al = len(alphabet)
    kl = len(keyword)
    for x in range(len(plaintext)):
        if plaintext[x] in alphabet:
            shift = ord(keyword[x % kl]) - ord("A")
            ciphertext += alphabet[(alphabet.find(plaintext[x]) + shift) % al]
        elif plaintext[x] in lalphabet:
            shift = ord(keyword[x % kl]) - ord("a")
            ciphertext += lalphabet[(lalphabet.find(plaintext[x]) + shift) % al]
        else:
            ciphertext += plaintext[x]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lalphabet = alphabet.lower()
    al = len(alphabet)
    kl = len(keyword)
    for x in range(len(ciphertext)):
        if ciphertext[x] in alphabet:
            shift = ord(keyword[x % kl]) - ord("A")
            plaintext += alphabet[(alphabet.find(ciphertext[x]) - shift) % al]
        elif ciphertext[x] in lalphabet:
            shift = ord(keyword[x % kl]) - ord("a")
            plaintext += lalphabet[(lalphabet.find(ciphertext[x]) - shift) % al]
        else:
            plaintext += ciphertext[x]
    return plaintext