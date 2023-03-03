'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''

class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def valoresPonto(self):
        print(f"valores: ({x},{y})")
    
class Retangulo:
    
    def __init__(self, verticePartida, largura, altura):
        self.largura = largura
        self.altura = altura
        self.verticePartida = verticePartida
    
    def centroRetangulo(self):
        pontoA = self.largura/2
        pontoB = self.altura/2
        print(f"O ponto central do retângulo é ({pontoA}, {pontoB})")

#construtor
while True:
    x = float(input("Informe o ponto x do vértice de partida: "))
    y = float(input("Informe o ponto y do vértice de partida: "))
    largura = float(input("Informe a lagura: "))
    altura = float(input("Informe a altura: "))
    verticePartida = Ponto(x, y)
    retangulo1 = Retangulo([verticePartida.x, verticePartida.y], largura, altura)
    retangulo1.centroRetangulo()
    escolha = input("Deseja refazer a operação? (s/n) ")
    if escolha == 's' or escolha == 'S':
        continue
    else:
        break
        
    
    
    
    
    
    
    
    
    