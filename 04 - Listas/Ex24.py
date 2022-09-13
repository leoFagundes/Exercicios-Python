"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados.
"""
import random

valorDado = []

def jogarDado(lista):
    lista.append(random.randint(1, 6))

for i in range (0, 100):
    jogarDado(valorDado)

print(valorDado)