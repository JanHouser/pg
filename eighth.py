def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5

    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)

    elif not isinstance(binarni_cislo, str):
        raise ValueError("Binární číslo musí být string nebo integer")

    if any(digit not in "01" for digit in binarni_cislo):
        raise ValueError("Binární číslo může obsahovat pouze 0 a 1")
    
    binarni_cislo = binarni_cislo[::-1]

    vaha = 1
    soucet = 0
    for digit in binarni_cislo:
        if digit == "1":
            soucet += vaha
        vaha = vaha * 2

    return soucet


        


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128