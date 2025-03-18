t1 = float(input("Teste 1: "))
t2 = float(input("Teste 2: "))
t3 = float(input("Teste 3: "))
p1 = float(input("Prova 1: "))
p2 = float(input("Prova 2: "))

cf = int()

notas = ["F", "D", "C", "B", "A"]

t = (t1 + t2 + t3) / 3
nf = (t / 5) + (0.4 * (p1 + p2))

if nf >= 5:
    cf += 1
    if nf >= 6:
        cf += 1
        if nf >= 7.5:
            cf += 1
            if nf >= 9:
                cf += 1

cfx = str(notas[cf])

print(f"{nf:.2f}")
print(cfx)