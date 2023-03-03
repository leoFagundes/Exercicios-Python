'''
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. 
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
'''

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.coin = 10
        self.saude = 100
        self.fome = 100
        self.felicidade = 100
    
    def status(self):
        def auxiliar(parametroSelf, frase80a100, frase60a80, frase40a60, frase20a40, frase0a20):
            if parametroSelf > 80 and parametroSelf <= 100:
                variavel = frase80a100
            elif parametroSelf >= 60 and parametroSelf <= 80:
                variavel = frase60a80
            elif parametroSelf >= 40 and parametroSelf < 60:
                variavel = frase40a60
            elif parametroSelf >= 20 and parametroSelf < 40:
                variavel = frase20a40
            else:
                variavel = frase0a20
            return variavel
        
        #saude     
        saude = auxiliar(self.saude, "Muito Saudável :D", "Saudável :)", "Razoavel :|", "Doente :(", "Morrendo x_x")
        
        #fome
        fome = auxiliar(self.fome, "Sem Fome :D", "Ok :)", "Com FOme :|", "Muita Fome :(", "Morrendo de Fome x_x")
        
        #felicidade
        felicidade = auxiliar(self.felicidade, "Extremamente Feliz :D", "Feliz :)", "Pra Baixo :|", "Triste :(", "Em Crise Existencial x_x")
        
        status = f'''
        ________________________
        {self.nome:^20}
        Saúde: {self.saude} -> {saude}
        Fome: {self.fome} -> {fome}
        Felicidade: {self.felicidade} -> {felicidade}
        Coins: {self.coin} coins
        ________________________
        '''
        print(status)

    def menu(self):
        menu = f'''
        _____________________
        {"MENU":^20}
        1) Visualizar Status
        2) Alimentar
        3) Brincar
        4) Fazer Carinho
        5) Levar ao Hospital
        _____________________
        '''
        print(menu)
    
    def brincar(self):
        print(f"Você está brincando com {self.nome}")
        self.saude -= 8
        if self.saude <= 0:
            print(f"{self.nome} morreu!")
            exit()
        self.fome -= 5
        if self.fome <= 0:
            print(f"{self.nome} está faminto.")
            print("Saude: -30")
            self.saude -= 30
            if self.saude <= 0:
                print(f"{self.nome} morreu!")
                exit()
        self.felicidade += 5
        if self.felicidade >= 100:
            self.felicidade = 100
            print(f"{self.nome} está muito feliz!")
        self.coin += 5
        print("Saude:       -8")
        print("Fome:        -5")
        print("felicidade:  +5")
        print("coins:       +5")
        
    def carinho(self):
        print(f"{self.nome} recebeu carinho")
        self.felicidade += 5
        print("Felicidade:  +5")
        print("coins:       +1")
        if self.felicidade >= 100:
            self.felicidade = 100
            print(f"{self.nome} está muito feliz!")
        self.coin += 1
        
#construtor
print("Vamos escolher o nome do seu pet.")
nome = input("nome: ")
pet = Tamagotchi(nome)
print(F"{pet.nome} nasceu!")

while True:
    while True:
        pet.menu()
        escolha = int(input("Escolha (1-5): "))
        if escolha == 1:
            pet.status()
            input("Tecle 'enter' para continuar.")
            break
        elif escolha == 2:
            while True:
                print(f'''{""}
                ALIMENTOS
                1) Frutas
                2) Massas
                3) Doces
                4) Voltar
                ''')
                escolha = int(input("Escolha (1-4): "))
                if escolha == 1:
                    while True:
                        print(f'''
                        FRUTAS (coins: {pet.coin})
                        1) Banana   | Fome: +5  | 5 coins
                        2) Maçã     | Fome:+6   | 6 coins
                        3) Melancia | Fome: +10 | 8 coins
                        4) Voltar
                        ''')
                        escolha = int(input("Escolha (1-4): "))
                        if escolha == 1:
                            if pet.coin < 5:
                                print("Dinheiro insuficiente para comprar banana.")
                                continue
                            else:
                                pet.coin -= 5
                                pet.fome += 5
                                print(f"{pet.nome} comeu uma banana")
                                print(f"Fome: +5")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 2:
                            if pet.coin < 6:
                                print("Dinheiro insuficiente para comprar maçã.")
                                continue
                            else:
                                pet.coin -= 6
                                pet.fome += 6
                                print(f"{pet.nome} comeu uma maçã")
                                print(f"Fome: +6")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 3:
                            if pet.coin < 6:
                                print("Dinheiro insuficiente para comprar melancia.")
                                continue
                            else:
                                pet.coin -= 8
                                pet.fome += 10
                                print(f"{pet.nome} comeu uma melancia")
                                print(f"Fome: +10")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 4:
                            break
                        else:
                            print("Opção inexistente, escolha novamente.")
                            continue
                if escolha == 2:
                    while True:
                        print(f'''
                        MASSAS (coins: {pet.coin})
                        1) Pizza    | Saúde: -10 | Fome: +14  | 8 coins
                        2) Macarrão | Saúde: -7 | Fome: +8   | 6 coins
                        3) Torrada  | Saúde: -5 | Fome: +5   | 3 coins
                        4) Voltar
                        ''')
                        escolha = int(input("Escolha (1-4): "))
                        if escolha == 1:
                            if pet.coin < 8:
                                print("Dinheiro insuficiente para comprar pizza.")
                                continue
                            else:
                                pet.coin -= 8
                                pet.fome += 14
                                pet.saude -= 10
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu uma pizza")
                                print(f"Fome:  +14")
                                print(f"Saúde: -10")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 2:
                            if pet.coin < 6:
                                print("Dinheiro insuficiente para comprar macarrão.")
                                continue
                            else:
                                pet.coin -= 6
                                pet.fome += 8
                                pet.saude -= 7
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu macarrão")
                                print(f"Fome:  +8")
                                print(f"Saúde: -7")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 3:
                            if pet.coin < 3:
                                print("Dinheiro insuficiente para comprar torrada.")
                                continue
                            else:
                                pet.coin -= 3
                                pet.fome += 5
                                pet.saude -= 5
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu uma torrada")
                                print(f"Fome:  +5")
                                print(f"Saúde: -5")
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 4:
                            break
                        else:
                            print("Opção inexistente, escolha novamente.")
                            continue
                if escolha == 3:
                    while True:
                        print(f'''
                        DOCES (coins: {pet.coin})
                        1) Donuts    | Felicidade: +10 | Saúde: -10 | Fome: +8  | 10 coins
                        2) Chocolate | Felicidade: +8  | Saúde: -7  | Fome: +5  | 7 coins
                        3) Bolo      | Felicidade: +6  | Saúde: -5  | Fome: +2  | 4 coins
                        4) Voltar
                        ''')
                        escolha = int(input("Escolha (1-4): "))
                        if escolha == 1:
                            if pet.coin < 10:
                                print("Dinheiro insuficiente para comprar donuts.")
                                continue
                            else:
                                pet.coin -= 10
                                pet.fome += 8
                                pet.saude -= 10
                                pet.felicidade += 10
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu um donuts")
                                print(f"Fome:       +14")
                                print(f"Saúde:      -10")
                                print(f"Felicidade: +10")
                                if pet.felicidade >= 100:
                                    print(f"{pet.nome} está muito feliz.")
                                    pet.felicidade = 100
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 2:
                            if pet.coin < 7:
                                print("Dinheiro insuficiente para comprar donuts.")
                                continue
                            else:
                                pet.coin -= 7
                                pet.fome += 5
                                pet.saude -= 7
                                pet.felicidade += 8
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu um chocolate")
                                print(f"Fome:       +5")
                                print(f"Saúde:      -7")
                                print(f"Felicidade: +8")
                                if pet.felicidade >= 100:
                                    print(f"{pet.nome} está muito feliz.")
                                    pet.felicidade = 100
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 3:
                            if pet.coin < 4:
                                print("Dinheiro insuficiente para comprar bolo.")
                                continue
                            else:
                                pet.coin -= 4
                                pet.fome += 2
                                pet.saude -= 5
                                pet.felicidade += 6
                                if pet.saude <= 0:
                                    print(f"{pet.nome} morreu!")
                                    exit()
                                print(f"{pet.nome} comeu um bolo")
                                print(f"Fome:       +2")
                                print(f"Saúde:      -5")
                                print(f"Felicidade: +6")
                                if pet.felicidade >= 100:
                                    print(f"{pet.nome} está muito feliz.")
                                    pet.felicidade = 100
                                if pet.fome >= 100:
                                    print(f"{pet.nome} está cheio.")
                                    pet.fome = 100
                                continue
                        if escolha == 4:
                            break
                        else:
                            print("Opção inexistente, escolha novamente.")
                            continue
                elif escolha == 4:
                    break
                else:
                    print("Opção inexistente, escolha novamente.")
                    continue
        elif escolha == 3:
            pet.brincar()
        elif escolha == 4:
            pet.carinho()
        elif escolha == 5:
            while True:
                print(f"""
                HOSPITAL coins: {pet.coin} | Vida atual: {pet.saude}
                1) Cura baixa: | +20 vida | 26 coins
                2) Cura alta:  | +60 vida | 50 coins
                3) voltar
                """)
                escolha = int(input("Escolha (1-3)"))
                if escolha == 1:
                    if pet.coin <= 26:
                        print("Dinheiro insuficiente.")
                        continue
                    else:
                        pet.coin -= 26
                        print(f"{pet.nome} foi curado.")
                        pet.saude += 20
                        if pet.saude >= 100:
                            pet.saude = 100
                            print(f"{pet.nome} está 100% curado")
                        print(f"Vida atual: {pet.saude}")
                elif escolha == 2:
                    if pet.coin <= 50:
                        print("Dinheiro insuficiente.")
                        continue
                    else:
                        pet.coin -= 50
                        print(f"{pet.nome} foi curado.")
                        pet.saude += 60
                        if pet.saude >= 100:
                            pet.saude = 100
                            print(f"{pet.nome} está 100% curado")
                        print(f"Vida atual: {pet.saude}")
                elif escolha == 3:
                    break
                else:
                    print("Opção inexistente, escolha novamente.")
                    continue
        else:
            print("Opção inexistente, escolha novamente.")
            continue




