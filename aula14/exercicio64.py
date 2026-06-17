#Criar um programa que léie varios números pelo teclado, o programa so pararar quando o usuario digitar 999, no final deve mostrar quantos números foram digitados e qual é a soma entre eles desconsiderando o número proposto para encerar o programa.
print('O programa so será encerrado quando o usuario digitar 999')
n = 0
c = 0
t = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        c += n
        t += 1 
print('A soma de todos os números digitados é {} em um total de {} números'.format(c ,t))