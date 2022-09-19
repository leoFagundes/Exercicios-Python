'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. 
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. 
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''

#altere o local do arquivo ao tentar rodar o código
def calcularTamanho(cod):
    tamanho = cod*434.99/456123789
    return tamanho

def padronizarLista(lista):
    global nomes
    global codigos

    listaProvisoria = []
    for item in lista:
        item = item.split()
        listaProvisoria.append(item)
        nomes.append(item[0])
        codigos.append(float(item[1]))

def percentual(codMB, total):
    percentual = codMB/total
    return percentual

#altere o local do arquivo ao tentar rodar o código
with open("E://Exercícios.py/07 - arquvios/Ex02/usuario.txt", "r", encoding='utf-8') as arquivo:
    df = arquivo.readlines()

nomes = []
codigos = []
padronizarLista(df)

for nome in nomes:
    if len(nome) > 15:
        print("ERROR: Nome com mais de 15 caractéres.") 
        exit()

texto = f"""ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
{'Nr.':<5}{'Usuário':^25}{'Espaço utilizado':^25}{'% do uso':^25}
"""

#altere o local do arquivo ao tentar rodar o código
#criar o novo arquivo chamado relatorio.txt
with open("E://Exercícios.py/07 - arquvios/Ex02/relatorio.txt", "w", encoding='utf-8') as relatorio:
    relatorio.write(texto)
    totalOcupado = 0
    for i, nome in enumerate(nomes):
        relatorio.write(f"{i:<5}{nome:^25}{f'{calcularTamanho(codigos[i]):.2f}':^25}{f'{percentual(codigos[i], sum(codigos)):.2%}':^25}\n")
        totalOcupado += calcularTamanho(codigos[i])
    relatorio.write(f"""
Espaço total ocupado: {totalOcupado:.2f} MB
Espaço médio ocupado: {totalOcupado/len(codigos):.2f} MB
    """)