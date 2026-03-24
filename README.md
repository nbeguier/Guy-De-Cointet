# Guy de Cointet — Projet de déchiffrement

Ce dépôt est dédié à l'exploration et au déchiffrement des œuvres chiffrées de l'artiste français **Guy de Cointet**. Connu pour son utilisation de lettres, de chiffres et de codes visuels, ce projet vise à percer les mystères de ses messages cryptés à l'aide d'outils linguistiques, algorithmiques et d'analyse littéraire.

---

## Structure du dépôt

- `xx.txt` : texte chiffré tel que trouvé dans l'œuvre.
- `xx.tips.txt` : indices ou annotations pour aider à la résolution.
- `xx.message.txt` : message clair déchiffré, si disponible.
- `README.md` : explications spécifiques à l'œuvre ou au dossier.
- `scripts/` : scripts Python pour le déchiffrement ou l'analyse.

---

## Œuvres

- **1971** — *Beige NSP EPE WAR* → `1971_Beige_NSP_EPE_WAR/`
- **1971** — *GSBHNFOUT* → `1971_GSBHNFOUT/`
- **1972** — *JEB OJO* → `1972_JEB_OJO/`
- **1973** — *Cizeghoh tur Ndjmb* → `1973_Cizeghoh_tur_Ndjmb/`
- **1973** — *Huzo Lumnst* → `1973_Huzo_Lumnst/`
- **1973** — Carnet VERT (COI 39) → `1973_VERT/`
- **1975** — *A Few Drawings* → `1975_A_few_drawings/`
- **Octogone** → `Octogone/`

---

## Scripts

- `search_pattern.py` — recherche de patterns de longueurs de mots dans un texte source.
- `vigenere.py` — chiffrement/déchiffrement par Vigenère.
- `decipher.py` — pipeline générique de déchiffrement.
- `all_rot.py` — application de ROT-n sur des textes.
- `anagrammes.py` — générateur d'anagrammes.
- `match_word_in_art.py` — recherche de mots dans les textes chiffrés.
- `test.sh` — vérifie que les messages déchiffrés connus sont retrouvés par `search_pattern.py`.

---

## Liens

- Discussions Reddit : [r/codes - Cizeghoh tur Ndjmb](https://www.reddit.com/r/codes/comments/12ewymq/guy_de_cointet_cizeghoh_tur_ndjmb)
- Carnets de Guy de Cointet : [guydecointet.org](http://guydecointet.org/en/carnet)

---

## Licence

Voir le fichier `LICENSE`.
