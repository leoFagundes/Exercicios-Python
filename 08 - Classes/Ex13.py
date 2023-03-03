'''
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
Escreva um pequeno programa que teste sua classe.
'''

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def informaNome(self):
        print(f"Nome do funcionário: {self.nome}")

    def informaSalario(self):
        print(f"Salário: R${self.salario}")

#construtor
funcionario1 = Funcionario('Leonardo', 1359.5)

funcionario1.informaNome()
funcionario1.informaSalario()

