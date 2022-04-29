'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

texto  = '''
Cardápio Lanchonete do seu ZÉ

Especificação   |Código  |  Preço
Cachorro Quente | 100    | R$ 1,20
Bauru Simples   | 101    | R$ 1,30
Bauru com ovo   | 102    | R$ 1,50
Hambúrguer      | 103    | R$ 1,20
Cheeseburguer   | 104    | R$ 1,30
Refrigerante    | 105    | R$ 1,00
'''

produtos = []
quantidades = []
precos = []

print(texto)

while True:
    print("")
    codigo = input("Digite o código do seu pedido: (exit) - para  sair do programa ")
    if codigo == 'exit':
        break

    if codigo == '100':
        qtde = int(input("Quantas unidades você vai querer de Cachorro quente? "))
        produtos.append('Cachorro quente')
        quantidades.append(qtde)
        precos.append(1.2*qtde)

    elif codigo == '101':
        qtde = int(input("Quantas unidades você vai querer de Bauru Simples? "))
        produtos.append('Bauru Simples')
        quantidades.append(qtde)
        precos.append(1.3*qtde)

    elif codigo == '102':
        qtde = int(input("Quantas unidades você vai querer de Bauru com ovo? "))
        produtos.append('Bauru com ovo')
        quantidades.append(qtde)
        precos.append(1.5*qtde)

    elif codigo == '103':
        qtde = int(input("Quantas unidades você vai querer de Hambúrguer? "))
        produtos.append('Hambúrguer')
        quantidades.append(qtde)
        precos.append(1.2*qtde)

    elif codigo == '104':
        qtde = int(input("Quantas unidades você vai querer de Cheeseburguer? "))
        produtos.append('Cheeseburguer')
        quantidades.append(qtde)
        precos.append(1.3*qtde)

    elif codigo == '105':
        qtde = int(input("Quantas unidades você vai querer de Refrigerante? "))
        produtos.append('Refrigerante')
        quantidades.append(qtde)
        precos.append(1.0*qtde)

    else:
        print("Item não encontrado, tente novamente.")
        continue

total = sum(precos)

print("")
for indice, i in enumerate(produtos):
    print(f"{i} x{quantidades[int(indice)]} = {precos[int(indice)]}")

print(f"Total: {total}")