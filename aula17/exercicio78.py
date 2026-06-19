#Criar um programa que leia 5 valores númericos e guarde em uma lista, No final mostre qual foi o maior valor digitado e suas respectivas posições na lista.
num = list()
for c in range (0, 5):
    num.append(int(input(f'Digite um número na posição {c}: ')))
print(f'Voce digitou os números {num}, ', end='')
print(f'O maior número foi {max(num)} na posição {num.index(max(num))} é o menor número foi {min(num)} na posição {num.index(min(num))}.')
print('FIM PROGRAMA')