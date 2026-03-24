#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


def parse_pattern(pattern_str: str) -> list[int]:
    try:
        lengths = [int(x) for x in pattern_str.split("-")]
    except ValueError:
        raise ValueError("Le motif doit être du type 1-3-6")

    if not lengths or any(n <= 0 for n in lengths):
        raise ValueError("Toutes les longueurs doivent être des entiers strictement positifs")

    return lengths


def normalize_text(text: str) -> list[str]:
    # Remplace tout caractère non alphanumérique par un espace
    # (ponctuation, apostrophes, tirets, etc.)
    cleaned = "".join(c if c.isalnum() else " " for c in text)

    # Réduit tous les espaces multiples à un seul séparateur
    words = cleaned.split()
    return words


def find_matching_sequences(words: list[str], pattern: list[int]) -> list[str]:
    matches = []
    n = len(pattern)

    for i in range(len(words) - n + 1):
        window = words[i:i + n]
        if all(len(word) == expected_len for word, expected_len in zip(window, pattern)):
            matches.append(" ".join(window))

    return matches


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Cherche dans un fichier texte les suites de mots correspondant "
            "à un motif de longueurs, par exemple 1-3-6."
        )
    )
    parser.add_argument("pattern", help='Motif, par exemple "1-3-6"')
    parser.add_argument("file", help="Chemin vers le fichier texte")

    args = parser.parse_args()

    try:
        pattern = parse_pattern(args.pattern)
    except ValueError as e:
        print(f"Erreur motif: {e}", file=sys.stderr)
        sys.exit(1)

    path = Path(args.file)
    if not path.is_file():
        print(f"Fichier introuvable: {path}", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(
            "Impossible de lire le fichier en UTF-8. "
            "Adapte l'encodage si nécessaire.",
            file=sys.stderr,
        )
        sys.exit(1)

    words = normalize_text(text)
    matches = find_matching_sequences(words, pattern)

    for match in matches:
        print(match)

    print(f"\nNombre total de correspondances: {len(matches)}", file=sys.stderr)


if __name__ == "__main__":
    main()
