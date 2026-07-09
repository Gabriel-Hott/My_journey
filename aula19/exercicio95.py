#Aprimorar o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
temp = dict()
gols = list()
final = list()
somagol = 0
while True:
    temp.clear()
    gols.clear()
    temp['nome'] = str(input('Nome: '))
    jogos = int(input(f'Quantos jogos o {temp['nome']} jogou: '))
    for c in range(0, jogos):
        gols.append(int(input(f'gols do {c + 1}° jogo: ')))
        somagol += gols[c]
    temp['gol'] = gols[:]
    temp['partida'] = sum(gols)
    final.append(temp.copy())
    while True:
        esc = str(input('Deseja continuar: [S/N] ').upper())
        if esc in 'SN':
            break
        print('Por favor escolha uma opcção VALIDA.')
    if esc in 'N':
        break
print(25 * '+=')
print(f'{'Indice dos Jogadores':^20}')
print(f'{'Nº':<4} | {'Nome':<15} | {'gol':<9} | {'Saldo gols':>11}')
for l, i in enumerate(final):
    print(f'{l:<4} | {i['nome']:<15} | {i['gol']} | {somagol:>11}')
while True:
    esc = int(input('Deseja ver mais sobre qual jogador: [SAIR 999] '))
    if esc == 999:
        break
    if esc >= len(final):
        print('Nº JOGADOR NÂO EXISTE POR FAVOR ESCOLHA UM VALIDO')
    else:
        print(f'BUSCA SOBRE -- jogador {final[esc]["nome"]}: ')
        for i, g in enumerate(final[esc]['gol']):
            print(f'Na partida {i + 1} fez {g} gols')
        print(40 * '+=')