'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:


    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def crescer(self, m):
        self.altura += m
        return self.altura


    def envelhecer(self, anos):
        for ano in range(1, anos+1):
            ano = 1
            if self.idade + ano < 21:
                self.altura = self.crescer(0.05)
                self.idade += ano
            else:
                self.idade += ano
        return self.idade


    def engordar(self, kg):
        self.peso += kg
        return self.peso

    
    def emagrecer(self, kg):
        self.peso -= kg
        return self.peso


#teste da classe
pessoa1 = Pessoa('Leo', 15, 65.5, 1.75)

print(pessoa1.altura)
print(pessoa1.envelhecer(2))
print(pessoa1.altura)

print(pessoa1.peso)
print(pessoa1.emagrecer(5))