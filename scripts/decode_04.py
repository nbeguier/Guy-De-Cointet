"""
Test de déchiffrement pour frame 04 : CRZERNODS-426
On teste toutes les combinaisons raisonnables :
  - substitution directe (sans Vigenère)
  - Vigenère addition mod 9 ou mod 10
  - Vigenère soustraction mod 9 ou mod 10
  - 0 = espace / 0 = lettre supplémentaire / 0 ignoré
"""

KEY_STR = "CRZERNODS"   # 9 lettres, positions 1-9
VIG_KEY = [4, 2, 6]

CIPHER_WORDS = [
    ["1288", "46"],
    ["375", "00182", "6", "9177"],
    ["8", "462", "35", "402083"],
    ["1995", "70"],
    ["20601394", "71", "573", "2", "04481", "62956", "304"],
    ["264", "01828!"],
]

def decode_digit(d, k, mode, mod):
    """Applique la clef Vigenère et retourne l'index dans KEY_STR (1-based)."""
    if mode == 'none':
        return d
    if mode == 'sub':
        r = (d - k) % mod
    else:  # add
        r = (d + k) % mod
    # ramener dans 1..9
    if r == 0:
        r = mod
    return r

def decode_line(words, mode, mod, zero_ch):
    result_words = []
    key_idx = 0
    for word in words:
        letters = []
        punct = ''
        w = word
        # isoler ponctuation finale
        while w and not w[-1].isdigit():
            punct = w[-1] + punct
            w = w[:-1]
        for ch in w:
            if ch == '0':
                letters.append(zero_ch)
                if zero_ch != '':
                    key_idx += 1
            elif ch.isdigit():
                d = int(ch)
                k = VIG_KEY[key_idx % 3]
                idx = decode_digit(d, k, mode, mod)
                if 1 <= idx <= len(KEY_STR):
                    letters.append(KEY_STR[idx - 1])
                else:
                    letters.append(f'[{idx}]')
                key_idx += 1
        result_words.append(''.join(letters) + punct)
    return ' '.join(result_words)

print(f"Clef : {KEY_STR}")
print(f"Mapping direct : {' '.join(f'{i+1}={c}' for i,c in enumerate(KEY_STR))}")
print()

# Paramètres à tester
modes = ['none', 'sub', 'add']
mods  = [9, 10]
zero_options = [('_', '_'), ('', '(skip)')]

for mode in modes:
    for mod in (mods if mode != 'none' else [9]):
        for zero_ch, zero_label in zero_options:
            label = f"mode={mode:4s}  mod={mod}  zero={zero_label}"
            lines = [decode_line(w, mode, mod, zero_ch) for w in CIPHER_WORDS]
            print(f"--- {label} ---")
            for l in lines:
                print(f"  {l}")
            print()
