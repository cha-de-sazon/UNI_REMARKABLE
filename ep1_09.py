a = int(500)
b = int(100)
c = int(25)
d = int(1)

carga = int(input("Carga: "))
pesos = [a, b, c, d]
caixas = []

for peso in pesos:
    peso2 = int(pesos.index(peso) - 1)
    caixa = (carga // peso) - ((pesos[peso2] // peso) * (carga // pesos[peso2]))
    caixas.append(caixa)

print(caixas)
