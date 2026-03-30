#!/bin/bash
# Teste tous les chiffrés de Cizeghoh tur Ndjmb sur un livre donné.
# Usage: bash scripts/search_book.sh <livre>
cd "$(dirname "$0")/.."

BOOK="$1"
DIR="1973_Cizeghoh_tur_Ndjmb"
PY="scripts/search_pattern.py"

if [ -z "$BOOK" ]; then
    echo "Usage: $0 <livre>"
    exit 1
fi

run() {
    local cipher="$1"; shift
    local out
    out=$(python3 "$PY" "$DIR/$cipher" "$BOOK" "$@" 2>&1)
    if echo "$out" | grep -q "occurrence(s)"; then
        echo "── $cipher $* ──"
        echo "$out" | grep -Ev "^Fichier|^Lignes|^Ponctuation"
        echo
    fi
}

# Sans --punct, --error 1
for f in 02_02.txt 04_03.txt 05_02.txt 05_05.txt 06_01.txt 06_02.txt 06_03.txt 09_02.txt 10_01.txt 10_04.txt 11.txt; do
    run "$f" --error 1
done

# Avec --punct, --error 1
for f in 02_02-1.txt; do
    run "$f" --punct --error 1
done

# Sans --punct
for f in 04_04.txt 05_01.txt 05_03.txt 05_04.txt 09_01.txt 09_03.txt10_05.txt; do
    run "$f"
done

# Avec --punct
for f in 02_04.txt 02_06.txt 03_01.txt 03_02.txt 03_03.txt 03_04.txt 04_05.txt 08_02.txt; do
    run "$f" --punct
done

# 10_02.txt trop long
