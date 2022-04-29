'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as 
temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []

for mes in meses:
    temperaturas.append(float(input(f"Qual a temperatura do mês de {mes}? ")))

mediaAnual = sum(temperaturas)/len(temperaturas)

print(f"\nA média anual de temperatura é de {mediaAnual} Graus")
print("A temperatura fica acima da média nos seguintes meses: ")

for i, temperatura in enumerate(temperaturas):
    if temperatura > mediaAnual:
        print(f"{meses[i]} - {temperatura} Graus")
