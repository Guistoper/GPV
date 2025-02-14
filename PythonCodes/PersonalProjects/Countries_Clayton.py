def linha():
    return("-" * 30)

def media(pais_densi, tamanho):
    pais_densi.sort()
    return pais_densi[tamanho - 1]

paises = [["Chipre", "Colômbia", "Comores", "República do Congo", "República Democrática do Congo"], 
          [1189265, 50372424, 806153, 5677493, 94660410], 
          [9251, 1138914, 1862, 342000, 2344858]]

paises_trans = [list(coluna) for coluna in zip(*paises)]
pais_nome = []
pais_popu = []
pais_area = []
pais_densi = []
pais_nome2 = []
pais_popu2 = []
pais_area2 = []
tamanho = len(pais_densi)

for i in range(len(paises_trans)):
    popu = paises[1][i]
    area = paises[2][i]
    densi = popu / area
    pais_popu.append(popu)
    pais_area.append(area)
    pais_densi.append(densi)

pais_media = media(pais_densi, tamanho)

for i in range(len(paises_trans)):
    print(linha())
    nome = paises[0][i]
    popu = paises[1][i]
    area = paises[2][i]
    densi = popu / area
    if pais_media == densi:
        pais_nome2.append(nome)
        pais_popu2.append(popu)
        pais_area2.append(area)
    print(f"Nome: {nome} \nPopulação: {popu} hab \nÁrea: {area} km² \nDensidade populacional: {densi} H/km²")

print(linha())
nome = pais_nome2[0]
print(f"País com maior densidade: {nome} \nDensidade populacional: {pais_media}")
print(linha())
print(f"Densidade média: {sum(pais_densi) / len(pais_densi)} H/km²")
print(f"População total: {sum(pais_popu)} hab")
print(f"Área total: {sum(pais_area)} km²")
print(linha())