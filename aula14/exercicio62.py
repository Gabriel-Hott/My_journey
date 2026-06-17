#Melhorar o exercicio 61, ele vai perguntar mais quantos termos o usúario quer até o usúario digitar '0' o programa será encerrado.
p1 = int(input('Qual é o primeiro termo: '))
raz = int(input('Qual é a razão: '))
c = 1
term = p1
total = 0
mais = 10
while mais != 0: 
    total += mais
    while c <= total: 
        print('{} - '.format(term), end='')
        term += raz
        c += 1
    print('Pausa')
    mais = int(input('Mais quantos termos deseja vêr: '))
print('FIM')