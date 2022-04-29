"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

m = (n1+n2)/2

if n1 < 0 or n1 >10 or n2 < 0 or n2 > 10:
    print("Média inválidas")
    exit()

if m >= 0 and m < 4:
    print("Suas notas foram {} e {}, sua média foi {}, seu conceito foi E\nVocê foi REPROVADO".format(n1, n2, m))
elif m >= 4 and  m < 6:
    print("Suas notas foram {} e {}, sua média foi {}, seu conceito foi D\nVocê foi REPROVADO".format(n1, n2, m))
elif m >= 6 and  m < 7.5:
    print("Suas notas foram {} e {}, sua média foi {}, seu conceito foi C\nVocê foi APROVADO".format(n1, n2, m))
elif m >= 7.5 and m < 9:
    print("Suas notas foram {} e {}, sua média foi {}, seu conceito foi B\nVocê foi APROVADO".format(n1, n2, m))
elif m >= 9 and m <= 10:
    print("Suas notas foram {} e {}, sua média foi {}, seu conceito foi A\nVocê foi APROVADO, parabéns!".format(n1, n2, m))
else: 
    print("Média inválidas")
    exit()