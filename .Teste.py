lista = ['alexandre       456123789\n', 'anderson        1245698456\n', 'antonio         123456456\n', 'carlos          91257581\n', 'cesar           987458\n', 'rosemary        789456125']

listaProvisoria = []
nome = []
codigo = []

for item in lista:
    item = item.split()
    listaProvisoria.append(item)
    nome.append(item[0])
    codigo.append(item[1])

print(nome)