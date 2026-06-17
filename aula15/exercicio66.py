#Criar um programa que leia varios números inteiros digitados pelo teclado, o programa deve ser encerrado quando o usuario digitar o número 999 é no final deve mostra a quantidade de números digitados e quanto e a soma deles.
print(30 * '+=')
print('O programa e encerrado automaticamente ao digitar (999)')
c = s = 0
print(30*'+=')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou um total de {c} números que somados dara o resultado {s}')
print(30 * '+=')
print('FIM PROGRAMA')