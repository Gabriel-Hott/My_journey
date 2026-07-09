#Criar um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador quantas partidas ele jogou.depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantos jogos: '))
if jogador['partidas'] > 0:
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Gols no jogo {c + 1}: ')))
        total += gols[c]
    jogador['gols'] = gols
    jogador['total'] = total
print(40 * '=+')
print(jogador)
print(40 * '+=')
for k, v in jogador.items():
    print(f'{k} tem {v}')
print(40 * '=+')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for l, c in enumerate(jogador['gols']):
    print(f'==> Na partida {l + 1} o jogador {jogador["nome"]} fez {c} gols')
print(f'No total de {jogador["total"]} gols')