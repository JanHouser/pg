def je_tah_mozny_pesec(pesec, cilova_pozice, obsazene_pozice):
    r, s = pesec
    r2, s2 = cilova_pozice

    if s2 != s or (r2, s2) in obsazene_pozice:
        return False
    if r2 == r + 1:
        return True
    if r == 2 and r2 == r + 2 and (r + 1, s) not in obsazene_pozice:
        return True
    
    return False

def je_tah_mozny_vez(vez, cilova_pozce, obsazene_pozice):
    r, s = vez
    r2, s2 = cilova_pozce

    if (r2, s2) in obsazene_pozice:
        return False
    
    if r != r2 and s != s2:
        return False
    
    if r == r2:
        for i in range(min(s, s2) + 1, max(s, s2)):
            if (r, i) in obsazene_pozice:
                return False
            
    else:
        for i in range(min(r, r2) + 1, max(r, r2)):
            if (i, s) in obsazene_pozice:
                return False
    return True

def je_tah_mozny_strelec(strelec, cilova_pozice, obsazene_pozice):
    r, s = strelec
    r2, s2 = cilova_pozice
    dr = r2 - r
    ds = s2 - s
    
    if abs(dr) != abs(ds) or (dr == 0 and ds == 0):
        return False
    
    krok_r = 1 if dr > 0 else -1
    krok_s = 1 if ds > 0 else -1

    for i in range(1, abs(dr)):
        mezilehla_pozice = (r + i * krok_r, s + i * krok_s)
        if mezilehla_pozice in obsazene_pozice:
            return False
        
    if cilova_pozice in obsazene_pozice:
        return False
    
    return True

def je_tah_mozny_jezdec(jezdec, cilova_pozice, obsazene_pozice):
    r, s = jezdec
    r2, s2 = cilova_pozice

    if (r2, s2) in obsazene_pozice:
        return False

    return (abs(r2 - r), abs(s2 - s)) in [(1, 2), (2, 1)]

def je_tah_mozny_dama(dama, cilova_pozice, obsazene_pozice):
    return (
        je_tah_mozny_vez(dama, cilova_pozice, obsazene_pozice)
        or je_tah_mozny_strelec(dama, cilova_pozice, obsazene_pozice)
    )

def je_tah_mozny_kral(kral, cilova_pozice, obsazene_pozice):
    r, s = kral
    r2, s2 = cilova_pozice

    dr = abs(r2 - r)
    ds = abs(s2 - s)

    if dr <= 1 and ds <= 1 and (dr != 0 or ds != 0):
        if cilova_pozice in obsazene_pozice:
            return False
        return True
    return False

def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    pozice = figurka["pozice"]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    if typ == "pěšec":
        return je_tah_mozny_pesec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "věž":
        return je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "jezdec":
        return je_tah_mozny_jezdec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return je_tah_mozny_kral(pozice, cilova_pozice, obsazene_pozice)


    
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True