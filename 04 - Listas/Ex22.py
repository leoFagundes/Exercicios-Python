"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

necessita da esfera;
necessita de limpeza; 
necessita troca do cabo ou conector; 
quebrado ou inutilizado.
Uma identificação igual a zero encerra o programa. 

Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

estadoMouses = []

print("""
Estado do mouse:

1- necessita da esfera;
2- necessita de limpeza; 
3- necessita troca do cabo ou conector; 
4- quebrado ou inutilizado.

0- sair
""")
while True:
    escolha = int(input(""))
    if escolha == 0:
        break
    elif escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
        estadoMouses.append(escolha)
    else:
        print("digite um valor válido.")
        continue

print(f"""
Quantidade de mouses: {len(estadoMouses)}

{'Situação':<40}{'Quantidade':^20}{'Percentual':^20}  
{'1- necessita da esfera':<40}{estadoMouses.count(1):^20}{f'{estadoMouses.count(1)/len(estadoMouses):.1%}':^20}
{'2- necessita de limpeza':<40}{estadoMouses.count(2):^20}{f'{estadoMouses.count(2)/len(estadoMouses):.1%}':^20}
{'3- necessita troca do cabo ou conector':<40}{estadoMouses.count(3):^20}{f'{estadoMouses.count(3)/len(estadoMouses):.1%}':^20}
{'4- quebrado ou inutilizado':<40}{estadoMouses.count(4):^20}{f'{estadoMouses.count(4)/len(estadoMouses):.1%}':^20}
""")