#Criar um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tul = 'Monitor', 998.90, 'Tv 40p', 999.99, 'Lapis', 1.50, 'Cane Suina', 56.76, 'Macacão', 128.90, 'Luva', 6.99, 'Mochila', 109.99
z = 1
print(40 * '-')
print(f'{'SUPER GA':^40}')
print(40 * '-')
for c in range (0, len(tul)):
    if c % 2 == 0:
        print(f'{tul[c]:.<30}', end='')
    else:
        print(f'R$ {tul[c]:.2f}')
