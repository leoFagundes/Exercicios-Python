'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''

n = int(input('Informe o n−ésimo termo da série de Fibonacci: '))
Fibonacci = [1]
k = 1

for i in range(1, n):
    Fibonacci.append(k)
    k = k + Fibonacci[i-1]
print(Fibonacci)

