import string

alphabet = string.ascii_lowercase
decrypted_message = ""
ciphertext = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
shift = 16

for letter in ciphertext:
    if letter.isalpha():  # Only decrypt alphabetic characters
        # Determine the ASCII base value (ord('a') or ord('A'))
        meaning = ord('a') if letter.islower() else ord('A')
        
        # Perform the shift and wrap around bounds if needed
        new_letter = (ord(letter) - meaning - shift) % 26 + meaning
        
        # Convert the ASCII value back to a character
        decrypted_message += chr(new_letter)
    else:
        # Leave non-alphabetic characters unchanged (like punctuation)
        decrypted_message += letter

print(decrypted_message)