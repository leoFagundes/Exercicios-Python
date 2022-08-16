"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

notas = []
notasString = []
ordinal = 0

while True:
    ordinal += 1
    nota = float(input(f"Digite a {ordinal}ª nota: (-1 para sair) "))
    if nota == -1:
        break
    notas.append(nota)
    notasString.append(str(nota))

print(f"As notas foram: {', '.join(notasString)}")

notas.reverse()
k = 0
print("Notas invertidas a ordem padrão:")
while True:
    if k == len(notas):
        break
    print(notas[k])
    k += 1
notas.reverse()

print(f"A soma das notas é: {sum(notas)}")

media = sum(notas)/len(notas)
print(f"A media das notas é: {media}")

acimaMedia = []
for x in notas:
    if x > media:
        acimaMedia.append(str(x))
print(f"Existem {len(acimaMedia)} valores acima da media: {', '.join(acimaMedia)}")

abaixoSete = []
for x in notas:
    if x < 7:
        abaixoSete.append(str(x))
print(f"Existem {len(abaixoSete)} valores abaixo de 7: {', '.join(abaixoSete)}")

texto = '''
---------------------------
    Programa Encerrado
---------------------------
'''
print(texto)