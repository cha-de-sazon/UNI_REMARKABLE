a = int(500)
b = int(100)
c = int(25)
d = int(1)

carga = int(input(":"))
pesos = [a, b, c, d]

caixas1 = [carga // peso for peso in pesos]

caixas = [caixas1[0], caixas1[1] - ((a // b) * caixas1[0]), caixas1[2] - ((b // c) * caixas1[1]), caixas1[3] - ((c // d) * caixas1[2])]

for i in caixas1:
    caixas = [caixas1[i] - ((pesos[n] // pesos[n+1]) * caixas1[i-1]) for n in pesos]

print(caixas)
