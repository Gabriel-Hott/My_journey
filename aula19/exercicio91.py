#Criar um programa ande 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rank = list()
print(f'{10*'+'}{'jogos':^10}{10*'+'}')
for k, i in jogo.items():
    print(f'{k} tirou {i} no dado')
    sleep(0.8)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{5*'+'}{' Placar dos melhores rankeados ':^25}{5*'+'}')
for i, v in enumerate(rank):
    print(f' - {i + 1}° lugar - {v[0]} com o jogo {v[1]}')
    sleep(0.7)   