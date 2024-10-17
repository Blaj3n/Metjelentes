# ['BP', 'ora', 'perc', 'szélirány', 'szélerősség',hőmérséklet]

def feladat(szam):
    print(f"\n{szam}. feladat")

metjelentes = []

with open("tavirathu13.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        metjelentes.append([str(egysor[0]), str(egysor[1][:2]), str(egysor[1][2:]), str(egysor[2][:3]),
        str(egysor[2][:3]), str(egysor[2][3:]), int(egysor[3])])

# print(metjelentes)
print(f"Egysor: {metjelentes[16]}")

feladat(2)
telepules = input("Adja meg egy település kódját! Település: ")
ido = []
for egyelem in metjelentes:
    if egyelem[0] == telepules:
        ido = []    # az 'ido' listánkat mindig kiürítem, így a legutolsó 'SM' adatnál az egészet szintúgy kiüríti, és beleteszi az utolsót. Így egy darab elemünk lesz benne.
        ido.append([egyelem[1], egyelem[2]])
print(ido)
print(f"Az utolsó mérési adat a megadott településről {ido[0][0]}:{ido[0][1]}-kor érkezett. ")
# print(f"Az utolsó mérési adat a megadott településről {ido[-1][0]}:{ido[-1][1]}-kor érkezett. ")