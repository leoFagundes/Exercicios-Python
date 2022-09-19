'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:


    def __init__(self, lado):
        self.lado = lado

    
    def mudar_lado(self, novoLado):
        self.lado = novoLado

    
    def mostrarLado(self):
        return self.lado


    def calcular_area(self):
        print(f"A área do quadrado é {self.lado * self.lado}")


#teste da classe
quadrado1 = Quadrado(9, 3)

print(quadrado1.mostrarLado())
quadrado1.calcular_area()
quadrado1.mudar_lado(4)
print(quadrado1.mostrarLado())
quadrado1.calcular_area()
