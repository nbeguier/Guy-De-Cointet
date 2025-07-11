import argparse

def decrypt(mapping_str, encrypted_text):
    # Build the substitution dictionary
    mapping = dict(pair.split('-') for pair in mapping_str.split(','))

    # Replace each character based on the mapping
    def replace(char):
        return mapping.get(char, '.')

    # Apply the mapping to each word
    words = encrypted_text.split()
    decrypted_words = [''.join(replace(c) for c in word) for word in words]

    return ' '.join(decrypted_words)

def main():
    parser = argparse.ArgumentParser(description="Decrypt a coded message using a character mapping.")
    parser.add_argument("mapping", help='Mapping string in the form "1-a,d-t,..."')

    args = parser.parse_args()
    encrypted_input = "01 234560 7898a23bc def049e dec 0g 32d4fc dec e4h6i6dj 07ck djle03 dec 78bd0kj de6390 21dck dec m61c n1"
    encrypted_input = "12 3456 7859 ab 6 4b5cd b6"
    encrypted_input = "74d9b6 ad4 19b6 edbf16b6 b9 8 g8h816 13 f4hed16b6"

    decrypted_output = decrypt(args.mapping, encrypted_input)
    print(decrypted_output)

if __name__ == "__main__":
    main()

