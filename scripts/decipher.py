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
    encrypted_input = "dec m61c n1 de6390 21dck dec 78bd0kj 07ck djle03 dec e4h6i6dj 0g 32d4fc def049e dec 7898a23bc 01 234560"
    encrypted_input = "01 2345 6748 9a5 3a4bca5 63cda5 9c30da5 ecaf05a5 ad 7 g7h705 02f3hec05a5"

    decrypted_output = decrypt(args.mapping, encrypted_input)
    print(decrypted_output)

if __name__ == "__main__":
    main()

