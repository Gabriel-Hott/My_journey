#Cria um programa que leia o nome e o preço de varios produtos. O programa deve perguntar se o usuário quer continuar ou não. No final mostre: 1 - Qual é o total gasto na compra. 2 - Quantos produtos custam mais de R$ 1000. 3 -  Qual é o nome do produto mais barato.
print(40 * '+=')
print(f'{'LOJA NADA BARATO':^70}')
print(40 * '+=')
tot = Vbara = caro = 0
c = 1
bara = ''
while True:
    nome = str(input('Qual o nome do produto: '))
    valor = float(input('Qual o valor do produto: R$'))
    if c == 1:
        Vbara = valor
        bara = nome
    c += 1
    if valor > 1000:
        caro += 1
    if valor < Vbara:
        Vbara = valor
        bara = nome
    tot += valor
    esc = str(input('Deseja continuar [S/N]: ')).upper().strip()[0] 
    if esc == 'N':
       break
    elif esc != 'S':
        print('Opção INVALIDA, por favor reinicie.')
print(f'O gasto total da compra foi {tot:.2f}, Ao todo {caro} produtos custaram mais de R$1000 e o produto mais barato foi o {bara}')