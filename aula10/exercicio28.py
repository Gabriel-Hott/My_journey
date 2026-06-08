#escrever um programa que faz o computador pensar em um numero INTEIRO entre 0 e 5 e peça para o usuario descobrir qual foi o numero, o programa deve escrever na tela se acertou ou não.
from random import randint
number = randint(0, 5)
print('Escolha um número de 0 a 5 e vejá se acerta oque a maquina escolheu')
n1 = int(input('Digite um número: '))
if number == n1:
    print('Parabens você ACERTOU!!! a maquina jogou {} e você {}'.format(number, n1))
else:
    print('Você PERDEU, pois a maquina escolheu {} e você {}'.format(number, n1))