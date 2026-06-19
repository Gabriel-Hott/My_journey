#Criar um programa que o usuario digite varios valores numéricos e cadastre-os em uma lista. Caso o número ja exista o programa deve desconsiderar o valor, No final o programa mostrar os valores unicos digitados em ordem crescente.
num = list()
while True:
    n = int(input('Digite um número: '))
    if num.count(n) == 0:
        num.append(n)
    else:
        print('NUMERO REPETIDO')
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
    elif r != 'S':
        print('OPÇÃO INVALIDA')
print(f'Os valores digitados em forma crescente são {sorted(num)}')