'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

vogais = ['A', 'E', 'I', 'O', 'U']
vetor = []

while len(vetor) < 10:
    char = input("Digite um caractere: ")
    if len(char) != 1:
        print("Digite APENAS UM caractere.")
        continue
    vetor.append(char.upper())
    
consoantes = 0
for i in vetor:
    if i not in vogais:
        consoantes += 1

print(f"Você digitou {consoantes} consoantes.")
