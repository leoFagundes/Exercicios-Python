'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:


    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self.material = material


    def mostraCor(self):
        return self.cor

    
    def trocaCor(self, novaCor):
        self.cor = novaCor


#teste da classe
bola_volei = Bola('branca', 1.2, 'plástico')

print(bola_volei.mostraCor())
bola_volei.trocaCor('preta')
print(bola_volei.mostraCor())
