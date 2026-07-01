#Faça um programa que leia o nome e peso de varias pessoas  e coloque tudo em uma lista. No final mostre: 1 - Quantas pessoas foram cadastradas. 2 - Uma listagem com as pessoas mais pesadas. 3 - Uma listagem com as pessoas mais leves.
temp = list()
pessoas = list()
p = l = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        p = l = temp[1]
    elif temp[1] > p:
        p = temp[1]
    elif temp[1] < l:
        l = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas')
print(f'O maior peso registrado foi {p}Kg, sendo o peso de ', end='')
for c in pessoas:
    if c[1] == p:
        print(f'{c[0]}', end='')
print()
print(f'O menor peso registrado foi {l}Kg, sendo o peso de ', end='')
for c in pessoas:
    if c[1] == l:
        print(f'{c[0]}', end='')