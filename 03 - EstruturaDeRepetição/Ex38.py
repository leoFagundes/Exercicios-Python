'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

salario = float(input("Digite o salário inicial do funcionário: "))
aumento_salarial = 1.5

ano_incial = 1996
ano_atual = 2022

for i in range(1, ano_atual - ano_incial):
    aumento_salarial *= 2

print(f"Em {ano_atual} o seu salário atual é de R${salario + salario*aumento_salarial/100:,}")

