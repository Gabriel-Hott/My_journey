#Cria um programa que jogue JOKENPÔ com o usuario.
from random import randint
print('{:=^40}'.format('Vamos jogar JOKENPÔ'))
print(""" ESCOLHA SUA MÃO
[0] PEDRA      
[1] PAPEL
[2] TESOURA""")
jogo = ('PEDRA', 'PAPEL', 'TESOURA')
mão = int(input('Escolha sua jogada: '))
if mão >= 3:
    print('Jogo INVALIDO')
cpu = randint(0, 2)
print(30* '=+')
print('a CPU jogou {} e o PLAYER jogu {} é o resutado foi... '.format(jogo[cpu], jogo[mão]), end='')
if cpu == 0:
    if mão == 1:
        print('PLAYER GANHOU')
    elif cpu == mão and mão == cpu:
        print('EMPATE')
    else:
        print('CPU GANHOU')
elif cpu == 1:
    if mão == 0:
        print('CPU GANHOU')
    elif cpu == mão and mão == cpu:
        print('EMPATE')
    else:
        print('PLAYER GANHOU')
else:
    if mão == 0:
        print('PLAYER GANHOU')
    elif cpu == mão:
        print('EMPATE')
    else:
        print('CPU GANHOU')
print(30* '=+')