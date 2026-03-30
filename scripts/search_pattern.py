#!/usr/bin/env python3
"""
Usage: python search_pattern.py <cipher_file> <text_file> [--context N] [--all] [--error N]

Extrait les longueurs de mots d'un fichier chiffré (groupes de chiffres séparés
par des espaces, sauts de ligne possiblement au milieu d'un mot) et cherche
les occurrences dans un fichier texte source.

La ponctuation attachée aux groupes (. ? ! ...) est extraite et utilisée pour
filtrer les matches : un match n'est retenu que si la ponctuation correspond.

Options:
  --context N   Nombre de mots de contexte avant/après (défaut: 8)
  --all         Afficher tous les matches, pas seulement les 5 premiers
  --punct       Filtrer par ponctuation (. ? ! ...) attachée aux groupes
  --error N     Accepter jusqu'à N mots avec une longueur incorrecte (fuzzy match)
"""

import re
import sys
import unicodedata
from itertools import product


def parse_cipher(filepath):
    """Extrait les groupes de chiffres et leur ponctuation depuis un fichier chiffré.
    Retourne : (lignes, ponctuation_finale)
    - lignes : liste de listes de longueurs de mots par ligne
    - punct  : dict {index_de_groupe_global -> ponctuation} pour les groupes
               suivis d'une ponctuation (.  ?  !  ...)
    """
    with open(filepath) as f:
        content = f.read().strip()
    lines = content.splitlines()

    result = []        # [[longueurs ligne1], [longueurs ligne2], ...]
    punct = {}         # {index_global -> ponct}
    global_idx = 0

    for line in lines:
        # Trouver chaque groupe de chiffres et la ponctuation qui le suit
        tokens = re.findall(r'(\d+)([.?!]|\.\.\.)?', line)
        lengths = []
        for digits, p in tokens:
            if not digits:
                continue
            lengths.append(len(digits))
            if p:
                punct[global_idx] = p
            global_idx += 1
        if lengths:
            result.append(lengths)

    if result:
        return result, punct

    # Fallback : si aucun chiffre trouvé, extraire les longueurs depuis les groupes de lettres
    for line in lines:
        tokens = re.findall(r'([a-zA-ZÀ-ÿ]+)([.?!]|\.\.\.)?', line)
        lengths = []
        for word, p in tokens:
            lengths.append(len(word))
            if p:
                punct[global_idx] = p
            global_idx += 1
        if lengths:
            result.append(lengths)

    return result, punct


def gen_patterns(lines):
    """Génère toutes les combinaisons de join/no-join aux sauts de ligne."""
    if len(lines) == 1:
        yield (), lines[0]
        return
    n_breaks = len(lines) - 1
    for joins in product([False, True], repeat=n_breaks):
        seq = list(lines[0])
        for i, join in enumerate(joins):
            next_line = list(lines[i + 1])
            if join:
                seq = seq[:-1] + [seq[-1] + next_line[0]] + next_line[1:]
            else:
                seq = seq + next_line
        yield joins, seq


def remap_punct(punct, cipher_lines, joins):
    """Recalcule les indices de ponctuation après application des joins."""
    # Construire la liste des groupes originaux avec leurs indices globaux
    flat = []
    for line in cipher_lines:
        flat.extend(line)

    # Construire le mapping original_idx -> new_idx après joins
    # (les groupes fusionnés héritent de la ponctuation du dernier groupe fusionné)
    remapped = {}
    new_idx = 0
    orig_idx = 0
    n_lines = len(cipher_lines)

    # Reconstruire en simulant les joins
    for line_i, line in enumerate(cipher_lines):
        for pos_in_line, length in enumerate(line):
            is_last_of_line = (pos_in_line == len(line) - 1)
            is_last_line = (line_i == n_lines - 1)
            join_next = (not is_last_line) and is_last_of_line and joins[line_i]

            if join_next:
                # Ce groupe va être fusionné avec le suivant : on ne crée pas de new_idx
                if orig_idx in punct:
                    remapped[new_idx] = punct[orig_idx]  # ponct provisoire
            else:
                if orig_idx in punct:
                    remapped[new_idx] = punct[orig_idx]
                new_idx += 1
            orig_idx += 1

    return remapped


def normalize(text):
    """Normalise le texte : supprime accents, remplace apostrophes par espace."""
    # Décomposer les ligatures (œ→oe, æ→ae, etc.) avant la normalisation
    text = text.replace('œ', 'oe').replace('Œ', 'OE')
    text = text.replace('æ', 'ae').replace('Æ', 'AE')
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = re.sub(r"[''`]", ' ', text)
    return text


def build_source(raw):
    """Retourne (words, lengths_array, word_punct) depuis le texte normalisé.
    word_punct[i] = ponctuation qui suit le mot i (ou None)."""
    # Rejoindre les mots coupés par tiret en fin de ligne
    raw = re.sub(r'(\w)-\n(\w)', r'\1\2', raw)
    # Tokeniser en gardant les mots ET la ponctuation adjacente
    tokens = re.findall(r"[a-zA-ZÀ-ÿ]+|[.?!]|\.\.\.", raw)
    words = []
    word_punct = {}
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if re.match(r'[a-zA-ZÀ-ÿ]', tok):
            word_idx = len(words)
            words.append(tok)
            # Regarder si le token suivant est une ponctuation
            if i + 1 < len(tokens) and re.match(r'^([.?!]|\.\.\.)$', tokens[i + 1]):
                word_punct[word_idx] = tokens[i + 1]
                i += 1  # consommer la ponctuation
        i += 1
    lengths_array = [len(w) for w in words]
    return words, lengths_array, word_punct


def find_pattern(lengths_array, word_punct, pattern, punct_filter, max_errors=0):
    """Cherche le pattern de longueurs + ponctuation dans le tableau précalculé."""
    n = len(pattern)
    target = tuple(pattern)
    results = []
    for i in range(len(lengths_array) - n + 1):
        window = lengths_array[i:i + n]
        errors = [j for j, (a, b) in enumerate(zip(window, target)) if a != b]
        if len(errors) > max_errors:
            continue
        # Vérifier la ponctuation
        match = True
        for offset, p in punct_filter.items():
            if offset >= n:
                continue
            actual = word_punct.get(i + offset)
            if actual != p:
                match = False
                break
        if match:
            results.append((i, errors))
    return results


def main():
    args = sys.argv[1:]
    context = 8
    show_all = False
    max_errors = 0

    if '--context' in args:
        idx = args.index('--context')
        context = int(args[idx + 1])
        args = args[:idx] + args[idx + 2:]
    if '--all' in args:
        show_all = True
        args.remove('--all')
    if '--error' in args:
        idx = args.index('--error')
        max_errors = int(args[idx + 1])
        args = args[:idx] + args[idx + 2:]
    use_punct = '--punct' in args
    if use_punct:
        args.remove('--punct')

    if len(args) < 2:
        print(__doc__)
        sys.exit(1)

    cipher_file, text_file = args[0], args[1]

    # Charger et normaliser le texte source
    with open(text_file) as f:
        raw = normalize(f.read())
    words, lengths_array, word_punct = build_source(raw)

    # Parser le fichier chiffré
    cipher_lines, punct = parse_cipher(cipher_file)
    if not cipher_lines:
        print("Aucun groupe de chiffres trouvé dans le fichier chiffré.")
        sys.exit(1)

    print(f"Fichier chiffré : {cipher_file}")
    print(f"Fichier source  : {text_file}")
    print(f"Lignes du chiffre : {cipher_lines}")
    if punct:
        print(f"Ponctuation détectée : {punct}")
    print()

    total_matches = 0
    seen_patterns = set()
    n_combos = 2 ** (len(cipher_lines) - 1)
    if n_combos > 64:
        print(f"(Attention : {n_combos} combinaisons de sauts de ligne à tester...)\n")

    for joins, pattern in gen_patterns(cipher_lines):
        key = tuple(pattern)
        if key in seen_patterns:
            continue
        seen_patterns.add(key)

        # Avec --punct, ne pas joindre un élément qui a une ponctuation terminale
        if use_punct and punct and joins:
            invalid = False
            g = 0
            for li, line in enumerate(cipher_lines[:-1]):
                last_g = g + len(line) - 1
                if joins[li] and last_g in punct:
                    invalid = True
                    break
                g += len(line)
            if invalid:
                continue

        punct_filter = remap_punct(punct, cipher_lines, joins) if (punct and use_punct) else {}
        hits = find_pattern(lengths_array, word_punct, pattern, punct_filter, max_errors)
        if not hits:
            continue

        join_desc = ''.join('J' if j else '_' for j in joins) if joins else 'n/a'
        punct_info = f"  ponct={punct_filter}" if punct_filter else ""
        print(f"Pattern {pattern}  [joins={join_desc}]{punct_info}  → {len(hits)} occurrence(s)")
        limit = len(hits) if show_all else min(5, len(hits))
        for idx, errors in hits[:limit]:
            ctx_before = ' '.join(words[max(0, idx - context):idx])
            ctx_after = ' '.join(words[idx + len(pattern):idx + len(pattern) + context])
            match_with_punct = []
            for j, w in enumerate(words[idx:idx + len(pattern)]):
                p = word_punct.get(idx + j, '')
                marker = '*' if j in errors else ''
                match_with_punct.append(marker + w + p + marker)
            print(f"  [{' '.join(match_with_punct)}]")
            print(f"   ...{ctx_before} >>> {' '.join(match_with_punct)} <<< {ctx_after}...")
        if not show_all and len(hits) > 5:
            print(f"  (+ {len(hits)-5} autres, utiliser --all pour tout afficher)")
        print()
        total_matches += len(hits)

    if total_matches == 0:
        print("Aucune occurrence trouvée.")


if __name__ == '__main__':
    main()
