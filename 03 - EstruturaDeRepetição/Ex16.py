'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.'''

n = int(input('Informe o n−ésimo termo da série de Fibonacci: '))
Fibonacci = [1]
k = 1

for i in range(1, n):
    if k > 500:
        Fibonacci.append(k)
        k = k + Fibonacci[i-1]
        break
    Fibonacci.append(k)
    k = k + Fibonacci[i-1]
print(Fibonacci)