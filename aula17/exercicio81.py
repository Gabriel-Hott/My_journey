#Criar um program que leia varios números em uma lista, No final mostre: 1 - Quantos números foram digitados, 2 - lista de valores  ordenados de forma decrecente, 3 -  se o valor 5 foi digitado é esta ou não na lista.
n = list()
while True:
    n.append(int(input(f'Digite um valor: ')))
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if 'N' in r:
        break
n.sort(reverse=True)
print(f'No total foram {len(n)} números digitados, Alinhados em forma decrecente {n} é o valor 5 ',end='')
if 5 in n:
    print(f'foi digitado o total de {n.count(5)} vezes.')
else:
    print('não foi digitado nessa rodada.')