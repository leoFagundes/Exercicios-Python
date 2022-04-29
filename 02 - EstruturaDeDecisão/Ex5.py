"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

n1 = float(input("Nota 1 (De 0 a 10): "))
n2 = float(input("Nota 2: (De 0 a 10): "))

media = (n1 + n2)/2

if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
    print("Uma ou mais notas são inválidas.")
else:
    if media >= 7 and media < 10:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com distinção")