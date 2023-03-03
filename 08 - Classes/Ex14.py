'''
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) 
que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
'''

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def informaNome(self):
        print(f"Nome do funcionário: {self.nome}")

    def informaSalario(self):
        print(f"Salário: R${self.salario}")
    
    def aumentarSalario(self, percent):
        self.salario += self.salario*percent/100
        print(f"Seu novo salário é de: {self.salario}") 

#construtor
funcionario1 = Funcionario('Leonardo', 1359.5)
funcionario1.aumentarSalario(10)
