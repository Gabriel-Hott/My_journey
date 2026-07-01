#Fazer um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
import time
c = 0
temp = list()
jogos = list()
print(30* '+=')
print(f'{'SENA PREMIADA':^60}')
print(30* '+=')
esc = int(input('Quantos jogos deseja jogar: '))
for r in range(0, esc):
    while True:
        rand = (int(randint(1, 60)))
        if rand not in temp:
            temp.append(rand)
            c += 1
        if c == 6:
            temp.sort()
            jogos.append(temp[:])
            temp.clear()
            c = 0
            break
for c in range(0, esc):
    print(f'Jogo {c + 1}: {jogos[c]}')
    time.sleep(0.8)
print(f'{'Boa sorte':^20}')