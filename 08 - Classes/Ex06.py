'''
Classe TV: 
Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class TV:


    def __init__(self):
        self.canal = 0
        self.volume = 30

    
    def numero_canal(self, valor):
        if valor <= 0 or valor > 99:
            print('Só existem canais de 1 a 99')
        else:
            self.canal = valor
            return self.canal
        
    
    def aumentar_volume(self, valor):
        if self.volume + valor > 100:
            return 'O volume máximo é 100'
        else:
            self.volume += valor
            return self.volume
    

    def diminuir_volume(self, valor):
        if self.volume - valor < 0:
            return 'O volume mínimo é 0'
        else:
            self.volume -= valor
            return self.volume


#teste da classe
tv = TV()


print(tv.numero_canal(20))

print(tv.aumentar_volume(30))
print(tv.aumentar_volume(30))

print(tv.diminuir_volume(20))
    