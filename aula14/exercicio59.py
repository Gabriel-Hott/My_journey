#Criar um programa que leie dois valores e depois mostre um menú aonde de 1 ao 5 contenha as seguintes alternativas ao usuario. 1 - SOMAR, 2 - MULTIPLICAR, 3 - MAIOR, 4 - NOVOS NÚMEROS, 5 - SAIR DO PROGRAMA. O programa deve realizar cada ação escolhida.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
esc = 0
while esc != 5:
    esc = int(input('[1] SOMAR OS NÚMEROS \n' \
    '[2] MULTIPLICAR OS NÚMEROS \n' \
    '[3] MAIOR NÚMERO\n' \
    '[4] NOVOS NÚMEROS\n' \
    '[5] SAIR DO PROGRAMA\n'))
    if esc == 1:
        final = n1 + n2
        print('A soma do {} + {} é igual a {}'.format(n1, n2, final))
    elif esc == 2:
        final = n1 * n2
        print('A multiplicação de {} X {} resultara em {}'.format(n1, n2, final))
    elif esc == 3:
        if n1 > n2:
            final = n1 
        else:
            final = n2
        print('O maior número entre {} e {} será o número {}'.format(n1, n2, final))
    elif esc == 4:
        n1 = int(input('Digite o primero número: '))
        n2 = int(input('Digite o segundo número: '))
print('FIM PROGRAMA')