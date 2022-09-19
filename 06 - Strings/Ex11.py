'''
Jogo de Forca. Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''
from random import choice

#altere o local do arquivo ao tentar rodar o código
with open("E://Exercícios.py/06 - Strings/forca.txt", "r") as palavrasTXT:
    palavras = []
    for palavra in palavrasTXT.readlines():
        palavras.append(palavra.replace("\n", ""))

#lista onde ficarão armazenadas as letras erradas
letrasErradas = []

#escolhendo uma palavra aleatório da lista palavras
palavraEscolhida = choice(palavras)
print("\nBem-vindo(a) ao jogo da forca.")
print("Uma palavra aleatória já foi escolhida, você tem 6 tentativas.")
tentativas = 0

#uma lista em que cada item é o caractere da palavra escolhida
listaPalavraEscolhida = []
#uma lista composta basicamente de de _ * len(palavraEscolhida)
listaPalavraOculta = []
#uma lista com as letras certas que foram escolhidas (serve apenas para quando a pessoa digitar a mesma letra duas vezes ele manda uma mensagem)
listaLetrasCertasEscolhidas = []

#preenchenco as listas
for letra in palavraEscolhida:
    listaPalavraEscolhida.append(letra)
    listaPalavraOculta.append('_')

#porgrama principal
while tentativas <= 6:
    print("-"*20)
    print(f"\nA palavra é: {' '.join(listaPalavraOculta)}")
    print(f"\nLetras erradas: {', '.join(letrasErradas)}")
    letra = input("Digite uma letra: ")
    letra = letra.casefold()
    #se a pessoa digitar mais de uma letra volta ao início para ela poder digitar outra
    if len(letra) != 1:
        print("\nDigite apenas uma letra.")
        continue
    #se a pessoa digitou uma letra errada repetida ela não perde uma tentativa, só aparece a mensagem abaixo
    elif letra in letrasErradas:
        print("\nVocê já digitou essa letra, presta atenção.")
        continue

    #se existe a letra digitada na palavra escolhida
    if letra in palavraEscolhida:
        if letra in listaLetrasCertasEscolhidas:
            print("\nVocê já digitou essa letra, presta atenção.")
            continue
        for i, novaLetra in enumerate(listaPalavraEscolhida):
            #se a letra escolhida for igual a novaLetra(uma letra da lista)
            if letra == novaLetra:
                #ele vai pegar o indice da palavra oculta e substituir o '_' pela letra
                listaPalavraOculta[i] = letra
                listaLetrasCertasEscolhidas.append(listaPalavraOculta[i])
        #se a lsitaPlavraOculta não tiver nenhum underline('_') a pessoa ganha o jogo
        if '_' not in listaPalavraOculta:
            print(f"\nMEUS PARABÉNS, você acertou a palavra '{palavraEscolhida}'.")
            exit()
    #se não existe a letra digitada na palavra escolhida
    else:
        if tentativas == 6:
            print(f"\nVocê perdeu. A plavara era: {palavraEscolhida}")
            exit()
        letrasErradas.append(letra)
        tentativas += 1
        print(f"\nVocê errou pela {tentativas}ª vez. Tente de novo!")