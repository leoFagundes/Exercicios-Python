"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""

n1 = float(input("Nota 1: "))
n2= float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3)/3

if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10 or n3 < 0 or n3 > 10:
    print("Uma ou mais notas são inválidas.")
else:
    if media >= 7 and media < 10:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com distinção")