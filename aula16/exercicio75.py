#Criar um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: 1 - Quantas vezes apareceu o valor 9, 2 - Em que posição foi digitado o primeiro valor 3, 3 - Quais foram os números pares.
tul = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o penútimo valor: ')), int(input('Digite o último valor: '))
Nov = 0
print(f'Os valores digitados foram {tul}, ', end='')

if tul.count(9) == 0:
    print('O número 9 não foi digitado', end='')
else: 
    print(f'O número 9 foi digitado o total de {tul.count(9)} vezes, ', end='')

if 3 in tul:
    print(f'O número 3 foi digitado na posição {tul.index(3)}º', end='') 
else:
    print(f', O número 3 não foi digitado', end='')

print(', E os números pares são')

for c in range (0, len(tul)):
    if tul[c] % 2 == 0:
        print(tul[c], end=', ')
print('\n FIM PROGRAMA')