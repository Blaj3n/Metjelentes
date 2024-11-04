# ['BP', 'ora', 'perc', 'szélirány', 'szélerősség',hőmérséklet]

def feladat(szam):
    print(f"{szam}. feladat")

metjelentes = []

with open("tavirathu13.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        metjelentes.append([str(egysor[0]), str(egysor[1][:2]), str(egysor[1][2:]), str(egysor[2][:3]),
        str(egysor[2][3:]), int(egysor[3])])

# print(metjelentes)
print(f"Egysor: {metjelentes[16]}")

feladat(2)
telepules = "SM"  #input("Adja meg egy település kódját! Település: ")
ido = []
for egyelem in metjelentes:
    if egyelem[0] == telepules:
        ido = []    # az 'ido' listánkat mindig kiürítem, így a legutolsó 'SM' adatnál az egészet szintúgy kiüríti, és beleteszi az utolsót. Így egy darab elemünk lesz benne.
        ido.append([egyelem[1], egyelem[2]])
# print(ido)
print(f"Az utolsó mérési adat a megadott településről {ido[0][0]}:{ido[0][1]}-kor érkezett. ")
# print(f"Az utolsó mérési adat a megadott településről {ido[-1][0]}:{ido[-1][1]}-kor érkezett. ")

feladat(3) # *
# homerseklet = []
# for egyelem in metjelentes:
#     homerseklet.append(egyelem[-1])
# print(homerseklet)

homerseklet = [egyelem[-1] for egyelem in metjelentes]
# print(homerseklet)

legk_hom = min(homerseklet)
legn_hom = max(homerseklet)
# print(legk_hom, legn_hom)
for egyelem in metjelentes:
    if egyelem[-1] == legk_hom:
        print(f"A legalacsonyabb hőmérséklet: {egyelem[0]} {egyelem[1]}:{egyelem[2]} {legk_hom} fok")
        break

for egyelem in metjelentes:
    if egyelem[-1] == legn_hom:
        print(f"A legmagasabb hőmérséklet: {egyelem[0]} {egyelem[1]}:{egyelem[2]} {legn_hom} fok")
        break

feladat(4)

szelcsend = False
for egyelem in metjelentes:
    if egyelem[3] == "000" and egyelem[4] == "00":
        szelcsend = True
        print(f"{egyelem[0]} {egyelem[1]}:{egyelem[2]}")

if not szelcsend: # == nem igaz TEHÁT hamis
    print("Nem volt szélcsend a mérések idején.")

# not valami -> valami == False
# valami -> valami == True

feladat(5)

telepulesek = []

for egyelem in metjelentes:
    if egyelem[0] not in telepulesek:
        telepulesek.append(egyelem[0])
print(telepulesek)

for telep in telepulesek: # telep == "BP"
    for egyelem in metjelentes:
        

"""
BP Középhőmérséklet: 23; Hőmérséklet-ingadozás: 8 
DC Középhőmérséklet: 29; Hőmérséklet-ingadozás: 15 
SM Középhőmérséklet: 22; Hőmérséklet-ingadozás: 8 
PA Középhőmérséklet: 21; Hőmérséklet-ingadozás: 7 
SN Középhőmérséklet: 26; Hőmérséklet-ingadozás: 13 
PR Középhőmérséklet: 21; Hőmérséklet-ingadozás: 8 
BC NA; Hőmérséklet-ingadozás: 14 
PP NA; Hőmérséklet-ingadozás: 6 
KE NA; Hőmérséklet-ingadozás: 13
"""


feladat(6)

telepulesek = []

for egyelem in metjelentes:
    if egyelem[0] not in telepulesek:
        telepulesek.append(egyelem[0])

# list comp.-ben nem lehet 'not in' feltételt írni, hisz a lista folyamatosan íródik.
for varos in telepulesek:
    with open(varos + ".txt", "w", encoding="utf-8") as fajl:
        fajl.write(varos + '\n')
        for elem in metjelentes:
            if elem[0] == varos:
                fajl.write(f"{elem[1]}:{elem[2]} {int(elem[4])*"#"}\n")