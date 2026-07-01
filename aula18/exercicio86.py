#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um número na linha {l + 1} e na coluna {c + 1}: ')))
print(25*'=+')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^3}', end='')
    print()