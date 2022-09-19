'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:


    def __init__(self):
        self.comprimento = 6
        self.largura = 3


    def mudar_valores(self, novoComprimento, novaLargura):
        self.comprimento = novoComprimento
        self.largura = novaLargura


    def mostrar_valores(self):
        print(f"comprimento: {self.comprimento}\nlargura: {self.largura}")
    

    def calcular_area(self):
        area = self.comprimento * self.largura
        return area


    def calcular_perimetro(self):
        perimetro = self.comprimento*2 + self.largura*2
        return perimetro
    

#teste da classe
ret = Retangulo()

ret.mostrar_valores()
print(ret.calcular_area())
print(ret.calcular_perimetro())

ret.mudar_valores(10, 3)
ret.mostrar_valores()
print(ret.calcular_area())
print(ret.calcular_perimetro())