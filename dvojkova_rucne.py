

cislo = int(input("Zadej nezáporné číslo:"))
def deleni(cislo):
    if cislo >0:
        cislo = cislo % 2
        return deleni(cislo)
    else:
        cislo = 0
    return cislo

print(f"Bin zapis cisla je{deleni(cislo)}")


