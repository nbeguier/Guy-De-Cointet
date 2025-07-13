from itertools import permutations

def rot_n(mot, n):
    """Applique ROT-n (chiffrement César) à un mot (lettres minuscules seulement)."""
    resultat = ''
    for c in mot:
        if 'a' <= c <= 'z':
            decale = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            resultat += decale
        elif 'A' <= c <= 'Z':
            decale = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
            resultat += decale
        else:
            resultat += c  # caractères non alphabétiques
    return resultat

def anagrammes(mot):
    """Renvoie tous les anagrammes uniques du mot."""
    return sorted(set(''.join(p) for p in permutations(mot)))

def rotn_et_anagrammes(mot):
    """Affiche ROT-n (1 à 25) du mot, et tous leurs anagrammes."""
    mot = mot.lower()
    for n in range(1, 26):
        rot = rot_n(mot, n)
        print(f"\nROT-{n} : {rot}")
        anas = anagrammes(rot)
        print("Anagrammes :", ', '.join(anas))

# Exemple d'utilisation
mot = "gioos"
rotn_et_anagrammes(mot)

