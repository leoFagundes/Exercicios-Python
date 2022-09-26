'''
Classe Macaco:
Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''

class Macaco:


    def __init__(self, nome):
        self.nome = nome
        self.bucho = 0.2

    
    def comer(self, comida, percent):
        if self.bucho + percent > 1:
            print(f"{self.nome.capitalize()} já está cheio.")
        else:
            self.bucho += percent
            print(f'{self.nome.capitalize()} foi alimentado com {comida}')
    

    def verBucho(self):
        print(f'O bucho de {self.nome.capitalize()} está {self.bucho:.0%} cheio')

    
    def digerir(self, percent):
        if self.bucho - percent < 0:
            print(f"{self.nome.capitalize()} está com fome demais para digerir isso.")
        else:
            self.bucho -= percent


#teste da classe
macaco1 = Macaco('macaco')
macaco2 = Macaco('Sofi')

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer('banana', 0.1)
macaco2.comer('maçã', 0.2)

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer('macarrão', 0.5)
macaco2.comer('inseto', 0.02)

macaco1.verBucho()
macaco2.verBucho()

macaco2.comer(macaco1.nome, 0.56)
macaco2.verBucho()

macaco2.digerir(0.8)
macaco2.verBucho()

