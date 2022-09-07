n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

divisoes = []

k = 2
while True:
    if n1 % k == 0 or n2 % k == 0:
        divisoes.append(k)
        if n1 % k == 0:
            n1 = n1/k
        if n2 % k == 0:
            n2 = n2/k
    else:
        k += 1
    if n1 == 1 and n2 == 1:
        break

resultado = 1
for x in divisoes:
    resultado = resultado * x

print(resultado)