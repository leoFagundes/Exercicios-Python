'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres "+" , "-" e "|".
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 40. 
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
'''

def retangulo(linha, coluna):
    if linha < 1:
        linha = 1
    if linha > 40:
        linha = 40
    if coluna < 1:
        coluna = 1
    if coluna > 40:
        coluna = 40

    print("+"*linha)
    for plus in range(1, coluna):
        print("+" + " "*(linha-2) + "+")
    print("+"*linha)

retangulo(40, 10)
