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

