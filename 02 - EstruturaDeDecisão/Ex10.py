"""Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

t = str(input("Em que turno você estuda? M-matutino ou V-Vespertino ou N-Noturno\n"))

if t == 'M' or t == 'm':
    print("Bom dia!")
elif t == 'V' or t == 'v':
    print("Boa tarde!")
elif t == 'N' or t == 'n':
    print("Boa noite!")
else:
    print("Valor inválido!")