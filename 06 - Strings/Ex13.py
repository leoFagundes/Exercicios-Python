'''
Jogo da palavra embaralhada. 
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
from random import shuffle, choice

#altere o local do arquivo ao tentar rodar o código
with open("E://Exercícios.py/06 - Strings/forca.txt", "r") as palavrasTXT:
    palavras = []
    for palavra in palavrasTXT.readlines():
        palavras.append(palavra.replace("\n", ""))

palavra = choice(palavras)

lista_palavra = []
for letra in palavra:
    lista_palavra.append(letra)
shuffle(lista_palavra)

tentativas = 0
while tentativas < 6:
    print(f"\nPalavra embaralhada: {' '.join(lista_palavra)}")
    resposta = input("Palavra certa: ")

    if resposta == palavra:
        print("\nVocê acertou!!")
        print(f"Palavra: {palavra}")
        break
    else:
        tentativas += 1
        if tentativas == 6:
            print("\nVOCÊ PERDEU!!")
            print(f"Palavra: {palavra}")
            break
        else:
            print("\nVocê errou.")
            print(f"Tentativas restantes: {6-tentativas}")
        
