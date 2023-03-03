'''
Classe Conta de Investimento: 
Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, 
com a diferença de que se adicione um atributo taxaJuros. 
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros 
(sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
'''

class ContaInvestimento:

    def __init__(self, numeroConta, nome, saldo, taxaJuros):
        self.numeroConta = numeroConta
        self.nome = nome
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionaJuros (self):
        print(f"Saldo: {self.saldo}\nAplicando juros...")
        self.saldo = self.saldo - self.saldo*self.taxaJuros
        print(f"Seu novo saldo é {self.saldo}\n")

#construtor
conta1 = ContaInvestimento('123', 'Leonardo Fagundes', 1000, 0.1)
conta1.adicionaJuros()
conta1.adicionaJuros()
conta1.adicionaJuros()
conta1.adicionaJuros()
conta1.adicionaJuros()