'''
Classe Conta Corrente: 
Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''


class ContaCorrente:


    def __init__(self, numero_conta, nome_correntista):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = 0


    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        return novo_nome

    
    def deposito(self, valor):
        self.saldo += valor
        
    
    def saque(self, valor):
        self.saldo -= valor


#teste da classe
conta_leo = ContaCorrente(1234, 'Leo')

print(conta_leo.nome_correntista)
print(conta_leo.alterar_nome('Pedro'))

print(conta_leo.saldo)
conta_leo.deposito(1000)
print(conta_leo.saldo)
conta_leo.saque(500)
print(conta_leo.saldo)
