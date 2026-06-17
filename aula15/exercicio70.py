#Cria um programa que leia o nome e o preço de varios produtos. O programa deve perguntar se o usuário quer continuar ou não. No final mostre: 1 - Qual é o total gasto na compra. 2 - Quantos produtos custam mais de R$ 1000. 3 -  Qual é o nome do produto mais barato.
print(40 * '+=')
print(f'{'LOJA CUSTA CARO':^70}')
print(40*'+=')
tot = 0
bara = ''
Vbara = 0
caro = 0
nome = str(input('Qual o nome do produto: '))
valor = float(input('Qual o valor do produto: R$'))
tot += valor
bara = nome
while True:
    esc = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    
    if esc == 'N':
       break
    else:
        nome = str(input('Qual o nome do produto: '))
        valor = float(input('Qual o valor do produto: R$'))
        tot += valor
        if valor >= 1000:
            caro += 1
        if valor < Vbara:
            bara = nome
print(f'O gasto total da compra foi {tot:.2f}, Ao todo {caro} produtos custaram mais de R$1000 e o produto mais barato foi o {bara}')