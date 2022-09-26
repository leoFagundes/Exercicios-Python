'''
Classe Bichinho Virtual:
Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. 
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, 
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Tamagushi():


    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 1

    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome


    def alterar_fome(self, fome):
        self.fome += fome
        return self.fome


    def alterar_saude(self, saude):
        self.saude += saude
        return self.saude


    def alterar_idade(self, idade):
        self.idade += idade
        return self.idade


#teste da classe
tamagushi = Tamagushi('Kaido')

print(tamagushi.alterar_nome('buggy'))
print(tamagushi.alterar_fome(5))
