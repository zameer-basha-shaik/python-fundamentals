import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

keys = chars.copy()

random.shuffle(keys)

plain_text = input("Enter text to encrypt: ")
encrypt_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypt_text += keys[index]

print(f"Encrypted text: {encrypt_text}")

decrypt_text = input("Enter text to decrypt: ")
plain_text = ""

for letter in decrypt_text:

    index = keys.index(letter)
    plain_text += chars[index]

print(f"Decrypted text: {plain_text}")

