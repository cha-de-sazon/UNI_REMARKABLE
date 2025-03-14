n = int(input("Numero:"))
enc = str("")

res = list(map(int, str(n)))

resx = [int((digit + 1) % 10) for digit in res]

resn = list(map(str, resx))

for digit in resn:
    enc = str(enc + digit)

encx = int(enc)

print(encx)
