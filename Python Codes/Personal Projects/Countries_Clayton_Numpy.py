import numpy as np

def linha():
    return "-" * 30

paises = np.array([
    ["Chipre", "Colômbia", "Comores", "República do Congo", "República Democrática do Congo"],
    [1189265, 50372424, 806153, 5677493, 94660410],
    [9251, 1138914, 1862, 342000, 2344858]
])

pais_nome = paises[0]
pais_popu = paises[1].astype(int)
pais_area = paises[2].astype(int)

pais_densi = pais_popu / pais_area

pais_densi_sorted = np.sort(pais_densi)
pais_media = pais_densi_sorted[-1]

filtro_maior_densidade = pais_densi == pais_media
pais_nome2 = pais_nome[filtro_maior_densidade]
pais_popu2 = pais_popu[filtro_maior_densidade]
pais_area2 = pais_area[filtro_maior_densidade]

for i in range(len(pais_nome)):
    print(linha())
    print(f"Nome: {pais_nome[i]} \nPopulação: {pais_popu[i]} hab \nÁrea: {pais_area[i]} km² \nDensidade populacional: {pais_densi[i]:.2f} H/km²")

print(linha())
print(f"País com maior densidade: {pais_nome2[0]} \nDensidade populacional: {pais_media:.2f}")
print(linha())
print(f"Densidade média: {pais_densi.mean():.2f} H/km²")
print(f"População total: {pais_popu.sum()} hab")
print(f"Área total: {pais_area.sum()} km²")
print(linha())
