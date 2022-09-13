'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

print("""
"Qual o melhor Sistema Operacional para uso em servidores?"

0- Sair

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
""")

SistOperacionais = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = []

while True:
    escolha = int(input(""))
    if escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6:
        print("Escolha uma opção válida.") 
        continue
    elif escolha == 0:
        break
    print(f"Você escolheu {SistOperacionais[escolha-1]}")
    votos.append(escolha)

votosSet = set()
for i in votos:
    votosSet.add(i)

votosSet = list(votosSet)
votosSet.sort()

print(f"\n{'Sistema Operacional':^20}{'Votos':^20}{'%':^20}")
for i in votosSet:
    print(f"{SistOperacionais[i-1]:^20}{votos.count(i):^20}{f'{votos.count(i)/len(votos):.1%}':^15}")

print(f"\n{'Total':^20}{sum(votos):^20}")