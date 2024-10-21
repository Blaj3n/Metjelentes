szam = 0
for i in range(1, 101):
    szam += i
print(f"Az első 100 szám összege: {szam}")

szamok = []
for k in range(1, 11):
    szamok.append(k)
print(f"Az első 10 szám listában: {szamok}")

paros_szamok = []
for szam in szamok:
    if szam % 2 == 0:
        paros_szamok.append(szam)
print(f"A páros számok a számok listában: {paros_szamok}")

# szam % 2 --> szam % 2 == 1
# List comprehension: lista lerövidítése
paros_szamok = [szam for szam in szamok if szam % 2 == 0]
print(f"A páros számok List Comp.-ben: {paros_szamok}")

# lista = [amit bele szeretnénk tenni, ciklus indítás, if feltétel]

paros_szamok = [int(szam) for szam in szamok if szam % 2 == 0 and szam % 4 == 0]
print(paros_szamok)


paratlan_szamok = [szam for szam in szamok if szam % 2]
print(f"Páratlan számok a számok listában:{paratlan_szamok}")

szamok_lista = [i for i in range(1,101) if i % 2 == 0]
print(szamok_lista)

szamok = [1, 2, 3, 4, 5, 6]
negyzet = [szam ** 2 for szam in szamok if szam % 3 == 0] # négyzetszámok szorzása: szam ** 2
print(negyzet)

szamok = [1, 2, 3, 4, 5, 6]
kob = [szam ** 3 for szam in szamok if szam % 3 == 0] # négyzetszámok szorzása: szam ** 2
print(kob)