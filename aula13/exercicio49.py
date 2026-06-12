#refazer o exercicio 9, faer uma tabuada de um número escolhido pelo usuario usando o laço FOR.
n = int(input('Digite o número que você deseja obter a tabuada: '))
for c in range(1, 10 + 1):
    print('[{}] x [{}] = {}'.format(c, n, c * n))