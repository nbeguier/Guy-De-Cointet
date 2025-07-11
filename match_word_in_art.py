import sys
import re
import itertools

def traiter_fichier(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()

    contenu = re.sub(r'[^a-zA-Z0-9\n]', ' ', contenu)
    contenu = contenu.replace('\n', '?')
    contenu = re.sub(r'\?{2,}', ' ', contenu)
    contenu = re.sub(r'\s\?\s', ' ', contenu)
    contenu = re.sub(r'\s\?', ' ', contenu)
    contenu = re.sub(r'\?\s', ' ', contenu)
    contenu = re.sub(r'^\?+|\?+$', '', contenu)
    contenu = re.sub(r'\s{2,}', ' ', contenu)
    contenu = contenu.strip()
    return contenu

def generer_tableaux_longueurs(texte_avec_question):
    indices = [m.start() for m in re.finditer(r'\?', texte_avec_question)]

    if not indices:
        mots = texte_avec_question.strip().split()
        return [list(map(len, mots))]

    resultats = set()
    n = len(indices)

    for pattern in itertools.product(['', ' '], repeat=n):
        texte_modifie = list(texte_avec_question)
        for idx, remplacement in zip(indices, pattern):
            texte_modifie[idx] = remplacement
        fusion = ''.join(texte_modifie)
        mots = fusion.strip().split()
        longueurs = tuple(len(m) for m in mots)
        resultats.add(longueurs)

    return sorted(resultats)

def phrase_vers_longueurs(phrase):
    phrase = re.sub(r'[^a-zA-Z0-9]', ' ', phrase)
    mots = phrase.strip().split()
    return [len(m) for m in mots]

def est_sous_sequence(sequence, sous_sequence):
    sous_sequence = tuple(sous_sequence)
    n, m = len(sequence), len(sous_sequence)
    for i in range(n - m + 1):
        if sequence[i:i + m] == sous_sequence:
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python script.py <fichier> <phrase>")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    phrase = sys.argv[2]

    resultat = traiter_fichier(nom_fichier)
    print(resultat)

    tableaux = generer_tableaux_longueurs(resultat)
    #print(tableaux)

    cible = phrase_vers_longueurs(phrase)

    print(f"Phrase : {phrase}")
    print(f"Longueurs de la phrase : {cible}\n")

    match = any(est_sous_sequence(tab, cible) for tab in tableaux)

    if match:
        print("✅ Sous-tableau trouvé dans au moins une combinaison.")
    else:
        print("❌ Aucune correspondance trouvée.")

