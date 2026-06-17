#Refaça o exercicio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progresão usando o while.
p1 = int(input('Qual é o primeiro termo: '))
raz = int(input('Qual é a razão: '))
c = 1
term = p1
while c <= 10:
    print('{} - '.format(term), end='')
    term += raz
    c += 1
print('FIM')