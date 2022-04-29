"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

TamanhoArq = float(input("Qual o tamanho do arquivo (em MB)? "))
VelocidadeLink = float(input("Qual a velocidade do link (em Mbps)? "))

temposegundos = TamanhoArq/(VelocidadeLink/8)

print("Seu download vai levar {} minutos".format(temposegundos/60))