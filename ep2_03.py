t1 = float(input("Teste 1: "))
t2 = float(input("Teste 2: "))
t3 = float(input("Teste 3: "))
p1 = float(input("Prova 1: "))
p2 = float(input("Prova 2: "))

cf = int()

notas = ["F", "D", "C", "B", "A"]
notas2 = [5, 6, 7.5, 9]

t = (t1 + t2 + t3) / 3
nf = (t / 5) + (0.4 * (p1 + p2))

for i in notas2:
    if nf >= i:
        cf += 1
    else:
        break

cfx = str(notas[cf])

print(f"{nf:.2f}")
print(cfx)
