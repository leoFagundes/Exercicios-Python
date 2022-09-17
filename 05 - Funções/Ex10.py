'''
Jogo de Craps. 
Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

ponto = 0

while True:
    input("\nEnter para jogar os dados")
    print("Você jogou os dados")
    resultado = dados()
    print(f"Valor da soma dos dados: {resultado}\n")
    if ponto == 0:
        if resultado == 7 or resultado == 11:
            print("----VOCÊ GANHOU----")
            break
        elif resultado in [2, 3, 12]:
            print("Craps")
            print("----VOCÊ PERDEU----")
            break
        elif resultado in [4, 5, 6, 8, 9, 10]:
            print("Você ganhou o ----PONTO----")
            ponto += 1
    elif ponto > 0:
        if resultado == 7:
            print("----VOCÊ PERDEU----")
            break
        elif resultado in [4, 5, 6, 8, 9, 10]:
            print("Você ganhou outro ----PONTO----")
            print("----VOCÊ GANHOU----")
            break