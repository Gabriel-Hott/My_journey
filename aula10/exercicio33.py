#fazer um programa que leie 3 numeros e mostre qual e o maior e qual e o menor
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
menor = n1
if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n3
print('O menor número foi {}'.format(menor))
maior = n1
if n2 > maior and n2 > n3:
    maior = n2
if n3 > maior and n3 > n2:
    maior = n3
print('O maior número digitado foi {}'.format(maior))