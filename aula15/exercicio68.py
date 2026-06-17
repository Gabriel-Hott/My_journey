#Fazer um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER. No final deve mostra o total de vitorias consecutivas que ele conquistou. (jogue o número e depois escolha entre par e impar)
from random import randint
soma = 0
c = 1
print(40 * '+=')
print('DESAFIO DO JOGO DA VELHA')
print(40 * '+=')
while True:
    soma = 0
    n = int(input('Qual número deseja jogar: '))
    esc = str(input('Escolha entre PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    if esc == 'P' or esc == 'I':
        pc = randint(0, 10)
        soma = n + pc
        print(f'Você jogou {n}º e o computador jogou {pc}, Somando dará {soma}', end=', ')
        if esc == 'P':
            if soma % 2 == 1:
               print(f'O jogo {c} deu IMPAR. você PERDEU!!!')
               break
            else:
                print(f'O jogo {c} deu PAR, você GANHOU!!!')
                c += 1
        else:
            if soma % 2 == 1:
                print(f'O jogo {c} deu IMPAR. você GANHOU!!!')
                c += 1
            else:
                print(f'O jogo {c} deu PAR. você PERDEU!!!') 
                break
    else:
        print('Escolha INVALIDA por favor escolha novamente!')
        print(40 * '+=')
print(40 * '+=')
print(f'Você jogou um total de {c} partidas até perder.')