#Aprimore o desafio anterior, mostrando no final: 1 - A soma de todos os valores pares digitados. 2 - A soma dos valores da terceira coluna. 3 - O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número na posição [{l + 1} {c + 1}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if l == 1:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
    print()
print(f'Soma dos pares {somapar}')
print(f'Soma dos valores da terceira coluna {soma3}')
print(f'O maior valor da segunda linha é {mai}')