import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lalphabet = alphabet.lower()
    al = len(alphabet)
    for i in plaintext:
        if i in alphabet:
            ciphertext += alphabet[(alphabet.find(i) + shift) % al]
        elif i in lalphabet:
            ciphertext += lalphabet[(lalphabet.find(i) + shift) % al]
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lalphabet = alphabet.lower()
    al = len(alphabet)
    for i in ciphertext:
        if i in alphabet:
            plaintext += alphabet[(alphabet.find(i) - shift) % al]
        elif i in lalphabet:
            plaintext += lalphabet[(lalphabet.find(i) - shift) % al]
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker_brute_force("python", d)
    0
    >>> caesar_breaker_brute_force("sbwkrq", d)
    3
    """
    best_shift = 0
    while best_shift < 26:
        if decrypt_caesar(ciphertext, best_shift) in dictionary:
            break
        else:
            best_shift += 1
    return best_shift