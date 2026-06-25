#Criar um programa aonde o usuário possa digitar 5 valores numéricos é cadastre-os em uma lista ja na posição correta (sem usar o sort()), No final mostre a lista ordenada na tela.
num = list()
for c in range(0, 5):
    n = (input('Digite um número: '))
    if c == 0:
        num.append(n)
    elif n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista')
    else:
        posi = 0
        while posi < len(num):
            if n <= num[posi]:
                num.insert(posi, n)
                print(f'Adicionado na posição {posi}')
                break
            posi += 1

print(f'Os valores digitados na ordem correta é {num}')