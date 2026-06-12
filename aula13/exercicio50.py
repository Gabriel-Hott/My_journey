#Fazer um programa que leia 6 números e some os númares PARES e desconsidere os números impares.
par = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par = par + n
print('A soma dos número PARES gerou o resutado de {}'.format(par))