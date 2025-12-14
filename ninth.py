def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    
    if isinstance(cislo, str):
        cislo = int(cislo)

    elif not isinstance(cislo, int):
        raise TypeError("Argument musí být int nebo str")

    result = ""        
    if cislo < 1:
        result += "0"
        return result

    
    vaha = 1
    while vaha * 2 <= cislo:
        vaha *= 2
    
    while vaha >= 1:

        if (cislo / vaha) >= 1:
            result += "1"
            cislo = cislo - vaha
        else: 
            result += "0"
        vaha = vaha / 2
    
    return result

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"