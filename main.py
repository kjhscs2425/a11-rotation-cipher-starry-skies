import string

alphabet = string.ascii_lowercase

# def encrypt(plaintext):
#     ciphertext = ""
#     for letter in plaintext:
#         old_position = alphabet.find(letter)
#         if old_position == -1:
#             ciphertext += " "
#         else:
#             new_position = old_position + key
#             new_position = new_position % len(alphabet)
#             new_letter = alphabet[new_position]
#             ciphertext += new_letter
#     return ciphertext

# print(encrypt(password))

# Your task:
# # figure out what key I used to encrypt this message:
# secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
# password = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
# key = 4
# def decrypt(password):
#     ciphertext = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
#     for letter in password:
#         old_position = alphabet.find(letter)
#         if old_position == -1:
#             ciphertext += " "
#         else:
#             new_position = old_position - key
#             new_position = new_position % len(alphabet)
#             new_letter = alphabet[new_position]
#             ciphertext += new_letter
#     return ciphertext

decrypted_message = ""
ciphertext = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
shift = 16

for letter in ciphertext:
    if letter.isalpha():  # Only decrypt alphabetic characters
        # Determine the ASCII base value (ord('a') or ord('A'))
        meaning = ord('a') if letter.islower() else ord('A')
        
        # Perform the shift and wrap within alphabet bounds
        new_letter = (ord(letter) - meaning - shift) % 26 + meaning
        
        # Convert the ASCII value back to a character
        decrypted_message += chr(new_letter)
    else:
        # Leave non-alphabetic characters unchanged
        decrypted_message += letter

print(decrypted_message)