import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()

    for i in plaintext:
        if i in alphabet:
            ciphertext += alphabet[alphabet.find(i) + shift]
        elif i in alphabet_low:
            ciphertext += alphabet_low[alphabet_low.find(i) + shift]
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()
    plaintext = ""

    for i in ciphertext:
        if i in alphabet:
            plaintext += alphabet[alphabet.find(i) - shift]
        elif i in alphabet_low:
            plaintext += alphabet_low[alphabet_low.find(i) - shift]
        else:
            plaintext += i

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    for shift in range(26):
        l = decrypt_caesar(ciphertext, shift)
        if l in dictionary:
            best_shift = shift
        break
    return best_shift
