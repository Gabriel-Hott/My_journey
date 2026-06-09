#Escrever um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem. 1 - o primeiro valor é MAIOR, 2 - o segundo valor é MAIOR, 3 - Não exite valor maior, os dois são iguais.
print(30 * '=')
print('Comparador de Números')
N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
if N1 > N2:
    print('O primeiro número é o MAIOR')
elif N1 < N2:
    print('O segundo número é o MAIOR')
else:
    print('Os numeros são IGUAIS')
print(30 * '=')