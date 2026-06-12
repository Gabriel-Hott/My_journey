#fazer um programa que mostre a soma de todos os números IMPARES que são múltiplos de 3 e que se encotram em um intervalo de 1 até 500.
soma = 0
vez = 0
for c in range (1, 501, 2):
    if c % 3 ==0:
        soma = soma + c
        vez = vez + 1
print('O total da soma dos númeos PRIMOS é {} do total de {} números.'.format(soma, vez))
print('fim programa')