def rot_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Messages chiffrés en dur
messages = ["GIOOS"]

# Affiche les 26 ROT pour chaque message
for shift in range(26):
    print(f"ROT{shift:02d}:")
    for msg in messages:
        decrypted = rot_decrypt(msg, shift)
        print(f"  {msg} -> {decrypted}")
    print()

