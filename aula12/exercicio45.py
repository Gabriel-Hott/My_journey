#Cria um programa que jogue JOKENPÔ com o usuario.
from random import randint
print('{:=^40}'.format('Vamos jogar JOKENPÔ'))
print(""" ESCOLHA SUA MÃO
[1] PEDRA      
[2] PAPEL
[3] TESOURA""")
jogo = ('PEDRA', 'PAPEL', 'TESOURA')
mão = int(2)
cpu = randint(1, 3)
print('{}PC, {}User'.format(jogo[cpu], jogo[mão]))
if cpu == mão:
    print('Jogo empatado CPU{} JOGADOR {}.'.format(jogo[cpu], jogo[mão])) 
elif cpu == 1 and mão == 2:
    print('Você venceu, CPU escolheu {}, JOGADOR escolheu {}'.format(jogo[cpu], jogo[mão]))
elif cpu == 2 and mão == 3:
    