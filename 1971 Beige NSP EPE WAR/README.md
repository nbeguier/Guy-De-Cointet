# 1971 – Beige NSP EPE WAR

Cette page sert de journal clair pour distinguer ce qui est en clair, ce qui est dechiffre, ce qui est partiel et ce qui reste a faire.

**Legende**
- **Clair**: texte present tel quel dans l'oeuvre.
- **Dechiffre**: solution obtenue.
- **Partiel**: solution incomplète ou hypothese forte mais pas verrouillee.
- **A faire**: non resolu.

Carnet original: https://www.guydecointet.org/carnet/270

---

## Page 1

**Chiffre**
```
NSP
EPE
WAR
```

**Dechiffre**
`NEWSPAPER` (lecture verticale)

---

## Page 2 – Cote gauche

**Chiffre**
```
PLTE
AMRE

PME
ATE
LR1

PMENIYN
ATEEFCT
LROFTES

APROBNBLYOHEO
FTHIGRESTPUIM
ENSMBERATHEMA
TICIUNEDOUARD
LFCASPARI2(18
41-189N)SPEET
I9YOARIKECTIN
GHISITWAAGIGT
NASKIUNTBLBAN
I9OPARI2OFLNL
OPQRCDLMPSTDC
HIATKSDECTARD
O8NLYOHE(12).
```

**Dechifree**
`PALMTREE`, `PALMTREE1`, `PALMTREE ONE FIFTY CENTS`

**Partiel (lecture plausible)**
`PROBABLY ONE OF THE GREAT PRIME NUMBER MATHEMATICIAN EDOUARD LUCAS (1841-1891)`

**Notes**
Reference implicite a Edouard Lucas.

**Piste de Recherche (tests deja faits)**

Structure du bloc :
- Carre 13×13 (169 caracteres), lettres + chiffres + `(`, `)`, `-`, `.`. Lettres absentes : `K`×3, `W`×1, `Q`×1.
- `EDOUARD` visible ligne 4, colonnes 7-13. Annees eclatees lignes 5-6 : `...2(18` / `41-189N)` → si N=1, `(1841-1891)` (Lucas ne en 1842).

Lectures testées :
- Colonnes (L→R / R→L), boustrophedon, diagonales, spirale : charabia.
- **Ligne par ligne** : seule lecture avec fragments anglais.

Comparaison ligne par ligne (texte cible) :
- Prefixe ~40 caracteres quasi correct, puis ecarts croissants (ex. pos 5 A→N, 10 N→H, 16 E→I, 20 A→S).
- Pas de decalage ROT uniforme ; pas de Vigenere courte (≤26) sur le prefixe.

Transposition :
- Methode PALMTREE validee sur blocs courts, mais echec sur 13×13 (y compris W=7, W=11, W=6 lignes de 13).

Tests supplementaires :
- Vigenere (cles : LUCAS, PRIME, PALMTREE, COINTET, GUY, EDOUARD, MATH, NUMBER, GREATEST, PROBABLY, FIBONACCI, LUCASPRIME, PRIMES) : rien de lisible.
- Suppression periodique (k=2..20) : meilleur partiel k=20 offset 1 ; insuffisant.
- Suppression positions premiers/Fibonacci/Lucas : rien de clair.
- Decimation mod 169 : aucun `PROBABLYONEOF`.
- Permutation de colonnes unique (13) optimisée sur 5 lignes : ≈25/65 corrects (insuffisant).
- Mapping chiffres→lettres (1→I, 2→S, 8→B, 9→G) : `PARI2`→`PARIS` plausible mais incoherent globalement.
- Alignement exact via suppression de nulles + mapping chiffres (digits en substitution) : aucun alignement complet.
- LCS : lettres-only 50/61 ; chiffres-wildcard 59/69.
- Chiffres traités comme chiffres : sequence `21841189992812` ; LCS chiffres = 8/8 avec `1841-1891` (vs 7/8 avec `1842-1891`) ; LCS alphanumerique 57/69 (1841-1891) vs 56/69 (1842-1891).
- Tests Hanoi / Lucas‑Lehmer :
  - Gray/Hanoi strict : ordre Gray sur 169 positions (8/9 bits, lecture row/col), + permutations lignes/colonnes via ordre Gray sur 0..12 ; LCS ≤ 48/69.
  - Lucas‑Lehmer positions : permutations par rang / par mod / par marche (p=5/7/11/13, row/col) ; LCS max 54/69.
  - Aucun gain vs baseline (LCS 57/69).
- Tests parcours/permutations locales :
  - Ordre carre magique 13×13 (Siamese), direct et inverse : pas d’amelioration.
  - Cisaillements (row shift k*r / col shift k*c, k=1..12) : LCS max 51/69.
  - Parcours par pas (primes/Lucas/Fibonacci) en 1D et en 2D : pas d’amelioration (LCS < baseline).
- Observations qualitatives (lecture ligne par ligne) :
  - `GREST` suggère **GREAT** (plutôt que GREATEST).
  - `MATHEMATICIUN` suggère **MATHEMATICIAN** avec permutation/substitution locale (M manquant apparent).
  - Après la date `(1841-1891)`, le texte devient nettement moins interpretable → probable fin de citation ou changement de mecanisme.

Pistes non encore testees :
- Permutation par cle a l’interieur de chaque ligne de 13 ?
- Les caracteres `K`, `W`, `Q` (nulles presumes) marquent-ils les positions switchees ?
- Substitution partielle : certaines lettres encodees (via alphabet octogonal p.10 du meme carnet ?), le reste en clair.
- Pistes Lucas possibles : Tour de Hanoi (ordre de deplacements / parcours binaire) comme chemin de lecture ou permutation.
- Pistes Lucas possibles : suite / test de Lucas‑Lehmer pour generer un flux numerique (mod 13) servant a permuter colonnes ou decaler par ligne.
- Pistes Lucas possibles : idees issues des *Recreations mathematiques* (parcours, taquin, carres magiques, dominos, labyrinthes) appliquees a une grille 13×13.

---

## Page 2 – Cote droit

**Chiffre (braille visuel)**
```
xx x. xx
xx .. .x
.. xx xx

xx x.
.x .x
.. ..

xx x. .x
.. .x x.
.. x. ..

xx .x x.
.x xx .x
x. x. ..
```

**Dechiffre**
`GUY DE COINTET`

---

## Page 3 – Cote gauche

Texte en hebreu.

**Notes**
Deux coupures de presse en yiddish (pas hébreu pur) collées sur la page gauche, provenant visiblement du journal The Forward (פֿאָרווערטס), le célèbre journal yiddish new-yorkais — confirmé par l'encart "Forward / Section 1 / 26 Pages / Price Twenty Five Cents" en bas à droite.

▎ האט איר געזוכט דעם זינגער א שענע פראוים?
▎ "Avez-vous cherché le chanteur, une belle femme ?" (approximatif)

---

## Page 3 – Cote droit

**Clair**
```
JOHNCAGENAMJUNEPAIKp89 AYEARFROMMONDAY
```

**Clair (citation)**
`Enjoy the commercials, that is to say, while you still have them.`

**Source**
John Cage et Nam June Paik. Citation de *A Year from Monday*, p. 89.

**Chiffree**
```
THEHEMEEMNTNOTNMQKTRSTVNO
```

**A faire**

**Notes**
texte anglais, écrit de droite à gauche selon l'hypothèse d'une inspiration yiddish, non déchiffré.

---

## Page 4

Texte en japonais.

---

## Page 5

**Clair**
```
The
Signature
Of
Mohammed
He used
to draw it
with his sword,
complete,
without raising
the blade
from
the ground.
```

**Notes**
Reference a la signature de Mahomet (dessinee sans lever la lame).
Voir exemple visuel: https://www.nga.gov/artworks/166114-signature-mohammed
	
**Clair**
`PACIFIC1`, `FIFTY CENTS`

**Chiffre (braille visuel)**
```
x. xx .x
x. .. .x
.x xx .x
```

**Dechiffree**: GUY

---

## Page 6

**Chiffree**
Cote gauche: matrice de lettres (`I?`, `E`, `A T`, etc.).

**A faire**

**Dechiffree**
Cote droit: `GUY DE COINTET`, `PACIFIC`.

---

## Page 7

Texte japonais.

**Clair**
`When radar was new it was found necessary to eliminate the balloon system for city protection that had preceded radar.`

---

## Page 8

**Clair**
Entrainement au chiffrement ROTx (contenu a identifier si besoin).

---

## Page 9

**A faire**
A completer.

---

## Page 10

**Clair**
Alphabet base sur des octogones (utilise ailleurs).

---

## Liens

- Carnet original: https://www.guydecointet.org/carnet/270
- John Cage – *A Year from Monday* (PDF): https://monoskop.org/images/a/a3/Cage_John_A_Year_from_Monday_New_Lectures_and_Writings.pdf
