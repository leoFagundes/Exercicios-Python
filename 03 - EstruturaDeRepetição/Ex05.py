'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

PopA = int(input('População A: '))
taxaPopA = float(input('Taxa de crescimento da Populção A: '))

PopB = int(input('População B: '))
taxaPopB = float(input('Taxa de crescimento da Populção B: '))

ano = 0

if PopB > PopA:
    while PopA < PopB:
        PopA += PopA*taxaPopA
        PopB += PopB*taxaPopB
        ano += 1
    print(f"A populção A demorou {ano} anos para ultrapassar a população B")
    print("População A: {:,.2f}".format(PopA))
    print("População B: {:,.2f}".format(PopB))
    exit()

if PopA > PopB:
    while PopB < PopA:
        PopA += PopA*taxaPopA
        PopB += PopB*taxaPopB
        ano += 1
    print(f"A populção B demorou {ano} anos para ultrapassar a população A")
    print("População A: {:,.2f}".format(PopA))
    print("População B: {:,.2f}".format(PopB))
    exit()