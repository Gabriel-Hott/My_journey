#Criar um programa onde o usuário possa digitar SETE valores númericos e cadastre-os em uma lista única que mantenha separados os valores impares e pares. No final mostre os valores pares e impares em ordem crescente.
num = [[], []]
for c in range(1, 8):
    res = int(input(f'Digite {c}° valor: '))
    if res % 2 == 0:
        num[0].append(res)
    else:
        num[1].append(res)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram {num[0]}, e os valores impares foram {num[1]}')