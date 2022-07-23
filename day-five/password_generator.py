"""
Program that generates a random password with letters, symbols, and numbers
"""
import random

letters: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols: list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters: int = int(input("How many letters would you like in your password?\n"))
nr_symbols: int = int(input("How many symbols would you like?\n"))
nr_numbers: int = int(input("How many numbers would you like?\n"))

new_pass: list = []

for i in range(0, nr_letters):
    new_pass += random.choice(letters)

for i in range(0, nr_symbols):
    new_pass += random.choice(symbols)

for i in range(0, nr_numbers):
    new_pass += random.choice(numbers)

random.shuffle(new_pass)

print("Here is your password:", end = " ")
print(*new_pass, sep = "")
