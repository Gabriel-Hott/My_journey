#Cria um programa que leia um numero INTEIRO e mostre se ele é PAR ou IMPAR.
n = int(input('Escreva qualquer numero para conferir se ele é par ou impar: '))
re = n % 2
if re == 0:
    print('O número {} é um número PAR'.format(n))
else:
    print('O numero {} é um número IMPAR'.format(n))