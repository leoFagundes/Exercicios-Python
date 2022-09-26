'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel

Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class BombaDeCombustivel:


    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel


    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if self.quantidade_combustivel - litros <= 0:
            return 'Combustível indisponível, abasteça a bomba'
        else:
            self.quantidade_combustivel -= litros
            return f'Foram abastecidos {litros} litros.\nQuantidade de combustível atual: {self.quantidade_combustivel}'


    def abastecer_por_litro(self, litros):
        valor = litros*self.valor_litro
        if self.quantidade_combustivel - litros <= 0:
            return 'Combustível indisponível, abasteça a bomba'
        self.quantidade_combustivel -= litros
        return f'{litros} litros de {self.tipo_combustivel}: R${valor}.\nQuantidade de combustível atual: {self.quantidade_combustivel}'


    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor


    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    
    def alterar_quantidade_combustivel(self, valor):
        self.quantidade_combustivel = valor


#teste da classe
bomba = BombaDeCombustivel('Gasolina', 5, 150)

print(bomba.abastecer_por_valor(25))
print(bomba.abastecer_por_litro(45))

bomba.alterar_quantidade_combustivel(50)
print(bomba.quantidade_combustivel)