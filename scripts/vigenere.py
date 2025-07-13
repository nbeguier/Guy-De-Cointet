import sys

def vigenere_numeric_key(message, key_digits, add=True):
    decrypted = ''
    key = [int(d) for d in key_digits]
    key_len = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = key[key_index % key_len]
            if not add:
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base + shift) % 26 + base)
            decrypted += decrypted_char
            key_index += 1
        else:
            decrypted += char  # conserver les espaces ou ponctuations

    return decrypted

def rotate_key(key):
    # Génère toutes les rotations circulaires possibles de la clé
    return [key[i:] + key[:i] for i in range(len(key))]

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <cipher> <clé numérique>")
        return

    key = sys.argv[2]

    encrypted_message = sys.argv[1] 

    print("Message original :", encrypted_message)
    print("")

    rotations = rotate_key(key)

    for i, rot in enumerate(rotations):
        result_add = vigenere_numeric_key(encrypted_message, rot, add=True)
        result_sub = vigenere_numeric_key(encrypted_message, rot, add=False)
        print(f"--- Rotation {i+1} (clé = {rot}) ---")
        print("  ➕ Ajout :", result_add)
        print("  ➖ Retrait :", result_sub)
        print("")

if __name__ == "__main__":
    main()

