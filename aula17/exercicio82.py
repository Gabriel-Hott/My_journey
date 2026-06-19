#Criar um programa que vai ler varios números e colocalos em uma lista. Depois disso, crie duas listas extras  que vão conter apenas os valores pares e os valores impares digitados, respectivamente. No final mostre o conteúdo das 3 listas.
l = list()
li = list()
lp = list()
while True:
    l.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if 'N' in r or 'n' in r:
        break
    elif r != 'S' or r != 's':
        print('Por favor escolha uma opção valida!')
for c in range (0, len(l)):
    if l[c] % 2 == 1:
        li.append(l[c])
    else:
        lp.append(l[c])  
print(f'Os números digitados foram {l}')
print(f'Os números impares são {li}')
print(f'Os números pares são {lp}')