#Melhorar o exercicio 61, ele vai perguntar mais quantos termos o usúario quer até o usúario digitar '0' o programa será encerrado.
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
c = 1
ter = p1
esc = 0
while esc != 1:
    print('{} - '.format(ter))
    ter += raz
    c += 1
    if c == 10:
        usu = str(input('Deseja ver mais termos desse número: [S/N]'))
        if usu == 'Ss':
            mais = int(input('Mais quantos números deseja ver: '))
        elif usu == 'Nn':
            esc = 1
            print('Fim dos termos')
