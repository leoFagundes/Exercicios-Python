'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.

Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. 

Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
'''

class Carro:


    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    
    def andar(self, km_andados):
        self.combustivel -= km_andados/self.consumo


    def obter_gasolina(self):
        return f'Nível atual de combustível: {self.combustivel:.2f} litros'


    def adicionar_gasolina(self, litros):
        self.combustivel += litros


#teste da classe
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionar_gasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
print(meuFusca.obter_gasolina())        # Imprime o combustível que resta no tanque.