"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

n1 = float(input("Número 1: "))
n2= float(input("Número 2: "))
n3 = float(input("Número 3: "))

ordem = [n1, n2, n3]

Maior = -99999999999999
Menor = 999999999999999
Medio = 0

if n1 > Maior:
    Maior = n1
    ordem[2] = n1
if n2 > Maior:
    Maior = n2
    ordem[2] = n2
if n3 > Maior:
    Maior = n3
    ordem[2] = n3

if n1 < Menor:
    Menor = n1
    ordem[0] = n1
if n2 < Menor:
    Menor = n2
    ordem[0] = n2
if n3 < Menor:
    Menor = n3
    ordem[0] = n3

if n1 != Maior and n1 != Menor:
    ordem[1] = n1
if n2 != Maior and n2 != Menor:
    ordem[1] = n2
if n3 != Maior and n3 != Menor:
    ordem[1] = n3

print (ordem)
    
        
