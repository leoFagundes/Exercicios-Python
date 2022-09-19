'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, 
contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

with open("E://Exercícios.py/07 - arquvios/Ex01/ederecoIP.txt", "r") as enderecosIP:
    enderecosIP = enderecosIP.readlines()

enderecos_validos = ['200.135.80.9', '192.168.1.1', '8.35.67.74', '1.2.3.4']
enderecos_invalidos = []

for end in enderecosIP:
    end = end.replace('\n', '')
    if end not in enderecos_validos:
        enderecos_invalidos.append(end)

with open("E://Exercícios.py/07 - arquvios/Ex01/ederecos validados.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("[Endereços válidos:]\n")
        arquivo.write("\n".join(enderecos_validos))
        arquivo.write("\n\n[Endereços inválidos:]\n")
        arquivo.write("\n".join(enderecos_invalidos))
