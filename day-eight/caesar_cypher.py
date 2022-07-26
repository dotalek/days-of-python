"""
Program to cypher and decypher a caesar shifted string of text.
"""

import sys

LOGO = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]

def encrypt(text: str, shift: int):
    """
    Encrypts a string of text by shifting it's characters a number of places forward on the
    alphabet. It wraps around as it reaches the end of the alphabet

    Parameters
    ----------
    text : str
        The user provided message to be encrypted
    shift : int
        The user provided number of places to shift each character in the message
    """
    cipher_text = ""
    for char in text:
        char_index = ALPHABET.index(char)
        new_index = (char_index + shift) % len(ALPHABET) # Wraps back around
        cipher_text += ALPHABET[new_index]
    print(f"The encoded text is {cipher_text}")

def decrypt(text: str, shift: int):
    """
    Decrypts a string of text by shifting its characters a number of places backwards on the
    alphabet. It wraps around as it reaches the beginning of the alphabet.

    Parameters
    ----------
    text : str
        The user provided message to be decrypted
    shift : int
        The user provided number of places to shift each character in the message
    """
    deciphered_text = ""
    for char in text:
        char_index = ALPHABET.index(char)
        new_index = (char_index - shift) % len(ALPHABET) # Wraps back around
        deciphered_text += ALPHABET[new_index]
    print(f"The decoded text is {deciphered_text}")

def caesar(direction: str, text: str, shift: int):
    """
    Encrypts or decrypts a string of text by shifting its characters a number of places forwards
    and backwards (respectively) on the alphabet. It wraps around as it reaches the beginning of
    the alphabet.

    Parameters
    ----------
    direction : str
        The direction the text should be shifted towards
    text : str
        The user provided message
    shift : int
        The user provided number of places to shift each character in the message
    """
    if direction == 'decode':
        shift *= -1
    shifted_text = ""
    for char in text:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            new_index = (char_index + shift) % len(ALPHABET) # Wraps back around
            shifted_text += ALPHABET[new_index]
        else:
            shifted_text += char
    print(f"The {direction}d text is {shifted_text}")

try:
    print(LOGO)
    while True:
        user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        user_text = input("Type your message:\n").lower()
        user_shift = int(input("Type the shift number:\n"))
        caesar(user_direction, user_text, user_shift)
        if input("Type 'yes' to process another message or 'no' to exit.\n").lower() == 'no':
            break
except KeyboardInterrupt:
    sys.exit()
