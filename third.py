def je_prvocislo(cislo):
   
   if cislo <= 1:
    return False
   
   if cislo == 2:
    return True
   
   for i in range(2, cislo):
      if cislo % i == 0:
         return False
   return True

if __name__ == "__main__":
    cislo = int(input("Zadej cislo: "))
    prvocisla = je_prvocislo(cislo)
    print(prvocisla)

def vrat_prvocisla(maximum):
    result = []

    aktualní = 0

    while aktualní < maximum:
     if je_prvocislo(aktualní):
      result.append(aktualní)
     aktualní += 1

    return result

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)

