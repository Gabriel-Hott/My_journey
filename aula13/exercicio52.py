#Fazer um programa que leia um número inteiro e diga se ele é ou não um número primo.
for c in range (1, 6):
    n = int(input('Digite um número e vejá se ele é um número primo: '))
    if n == 2 or n % 2 == 1 :
        if  n >1 and n % n == 0 and n % 1 == 0 or n == 2:
            print('O número {} é um número PRIMO'.format(n))
        else:
            print('O número {} NÂO é um número primo'.format(n))
    else:
        print('O número {} NÂO é um número primo'.format(n))