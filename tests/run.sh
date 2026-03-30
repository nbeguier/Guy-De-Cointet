#!/bin/bash
# Regression tests for search_pattern.py
cd "$(dirname "$0")/.."

PASS=0; FAIL=0

check() {
    local desc="$1" expected="$2"; shift 2
    local out; out=$("$@" 2>&1)
    if echo "$out" | grep -qF "$expected"; then
        echo "PASS  $desc"
        ((PASS++))
    else
        echo "FAIL  $desc"
        echo "      attendu : $expected"
        ((FAIL++))
    fi
}

# ── fake_book (tests de ponctuation) ──────────────────────────────────────
check "03_01 --punct" "[ET MAGDA? TOUT JUSTE!]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/03_01.txt tests/fake_book.txt --punct

check "03_02 --punct" "[NICOLAS ET ALEX? AH!]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/03_02.txt tests/fake_book.txt --punct

check "03_03 --punct" "[CET ENFANT? OUI MESSIRE II.]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/03_03.txt tests/fake_book.txt --punct

check "03_04 --punct" "[PERDU? SEMAINE.]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/03_04.txt tests/fake_book.txt --punct

check "08_01" "[Toi et Pierrott]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/08_01.txt tests/fake_book.txt

check "08_02 --punct" "[Marie a pris une bicyclette rouge.]" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/08_02.txt tests/fake_book.txt --punct

# ── vrais livres ───────────────────────────────────────────────────────────
check "02_01 Litt_potentielle --error 1" "occurrence(s)" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/02_01.txt books/Litt_potentielle-Oulipo-1973.txt --error 1

check "02_03 Litt_potentielle" "occurrence(s)" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/02_03.txt books/Litt_potentielle-Oulipo-1973.txt

check "02_03 Odile (Queneau)" "occurrence(s)" \
    python3 scripts/search_pattern.py 1973_Cizeghoh_tur_Ndjmb/02_03.txt books/Odile-Queneau-1937.txt

# ──────────────────────────────────────────────────────────────────────────
echo ""
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
